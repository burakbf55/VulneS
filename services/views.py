import os

from django.shortcuts import render


def nmap_to_command(target, filename ,ports, arguments):
    nmap_command = "/usr/bin/nmap "+ ports + " " + arguments + " " + target + " " + "-oX" + " " + "/code/media/xml/" + filename + ".xml" 
    
    os.system(nmap_command)
    print(nmap_command)
    while True:
        if os.path.exists("/code/media/xml/" + filename + ".xml"):
            break
        else:
            continue
    
    return nmap_command