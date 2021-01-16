import requests
from bs4 import BeautifulSoup
import pandas
from matplotlib import pyplot as plt
import numpy as np
import csv



data=[]  # // Creating a dictonary
prices=[]
base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,30,10):
    # // Send request to the website with headers in order to trick the website and act like "User-agent"
    r= requests.get(base_url+str(page)+".html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c= r.content
    # // Define "soup" as html
    soup = BeautifulSoup(c, "html.parser")
    # // Search for the class "propertyRow" which is the main class
    all = soup.find_all("div", {"class": "propertyRow"})
# // Build a "for" loop that gather information from the html code.
    for item in all:
        d={}
        d["Price"] = item.find("h4", {"class": "propPrice"}).text.replace("\n", "".replace("", ""))  # Find class "propPrice" and remove empty spaces.
        d["Address"] =item.find_all("span",{"class": "propAddressCollapse"})[0].text # Find class "propAddressCollapse"
        d["Locality"] =item.find_all("span",{"class": "propAddressCollapse"})[1].text # Find class "propAddressCollapse"
        try:
            # Since some of the objects in "propertyRow" class have no value for "infoBed":
            # Try to find "infoBed" class and if the class was not found , pass.
            # Ignoring this stage will raise an error
            d["Beds"] =item.find("span",{"class", "infoBed"}).find("b").text
        except:
            d["Beds"] = "None"
            pass
        try:
            d["FullBaths"] =item.find("span",{"class", "infoValueFullBath"}).find("b").text
        except:
            d["FullBaths"] = "None"
            pass
        try:
            d["HalfBaths"] =item.find("span", {"class", "infoValueHalfBath"}).find("b").text
        except:
            d["HalfBaths"] = "None"
            pass
        try:
            d["Area"] =item.find("span",{"class", "infoSqFt"}).find("b").text
        except:
            d["Area"] = "None"
            pass
        # Since there are few classes with the same name the code will react to all of them.
        # To solve this we made a another "for" loop inside "for loop".
        for column_group in item.find_all("div", {"class": "ui-column"}): # Search in class "ui-column"
            # Inside "ui-column" , search for the class "featureGroup" *and* "featureName"
            # Using "zip" feature allows us to search inside 2 "containers" instead of one.
            # This way we can specify what we want to get instead of getting all the content of the class
            for feature_group, feature_name in zip(column_group.find_all("span",{"class": "featureGroup"}),column_group.find_all("span",{"class": "featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] =feature_name.text
        data.append(d)   # // Adding all the information from the loop to the "data" dictonary.
        prices.append(d["Price"])

# // Organize "data" into data frame using panada and convert it to CSV file.
df = pandas.DataFrame(data)
df.to_csv("output.csv")
clean_data = []
for row in prices:
    wanted_text = row.split("$")[1].split(" ")[0].replace(",","")
    clean_data.append(wanted_text)


#height = clean_data
data_len = len(list(data))
# Make a fake dataset:

test=[]
i =0
for o in range(0,data_len):
    i+=1
    print(i)
    test.append(i)


bf = pandas.DataFrame({'Count':test, 'Prices':clean_data})
bf=bf.astype(float)

ax = bf.plot.bar(x='Count', y='Prices', rot=0)
plt.show()