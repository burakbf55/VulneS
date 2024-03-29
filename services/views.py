import os


def nmap_to_command(target, filename ,ports, arguments):
    if ports:
        nmap_command = "nmap " + ports + " " + arguments + " " + target + " " + "-oX" + " " + "/code/media/xml/" + filename + ".xml"
    else:
        nmap_command = "nmap " + arguments + " " + target + " " + "-oX" + " " + "/code/media/xml/" + filename + ".xml" 
    
    os.system(nmap_command)
    print(nmap_command)
    while True:
        if os.path.exists("/code/media/xml/" + filename + ".xml"):
            break
        else:
            continue
    
    return nmap_command