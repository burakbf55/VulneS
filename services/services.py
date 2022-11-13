from nmap import nmap


class NmapService():
    def __init__(self, target, options):
        self.target = target
        self.options = options
    
    def nmap(target, ports= None, arguments='-sV',
             sudo=False, timeout=0):
        nm = nmap.PortScanner()
        result = nm.scan(target, ports, arguments)

        return result