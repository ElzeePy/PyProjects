import socket
import termcolor
import time

def scan(target,ports):
    print(termcolor.colored("\n" + ' Starting Scan For ' + str(target),'red'))
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened: " + str(port))
        sock.close()
    except:
        pass
print(termcolor.colored("[*] Enter Targets To Scan (split them by ,): ",'blue'))
targets = input(termcolor.colored("-->",'blue'))
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if "," in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))
    for ip_addr in targets.split((",")):
        scan(ip_addr.strip(''),ports)
else:
    scan(targets,ports)
