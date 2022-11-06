from nmap import nmap

class NmapService():
    def __init__(self, target, options):
        self.target = target
        self.options = options
    
    def nmap(target,options):
        nm = nmap.PortScanner()
        result = nm.scan(target, options)

        return result