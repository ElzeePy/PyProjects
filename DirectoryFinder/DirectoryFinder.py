import requests
import termcolor

print(f'-----------=====DirectoryFinder=====-----------')
print(f'---------------Created by **** ----------------')
print(termcolor.colored("\nUsage Example: Facebook.com",'green'))
print("")

target_url = input(termcolor.colored("[*] ",'blue')+ "Enter Target URL: ")
print("")
file_name = "./DirDB.txt"


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

file = open(file_name, 'r')
for line in file:
    directory = line.strip()
    full_url = target_url + '/' + directory
    response = request(full_url)
    if response:
        print(termcolor.colored('[+]','red'), 'Discovered Directory At This Path: ' + termcolor.colored(full_url,'green'))

