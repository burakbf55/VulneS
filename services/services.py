from nmap import nmap


class NmapService():
    def __init__(self, target, options):
        self.target = target
        self.options = options
    
    def nmap(target, ports= None, arguments='-sV',
             sudo=False, timeout=0):
        nm = nmap.PortScanner()
        nm.scan(target, ports, arguments)
        com_line = nm.command_line()
        scan_method = nm.scaninfo().get('method')
        host_up_or_down = nm[target].state()
        scan_protocol_tcp = nm[target].all_protocols()
        print(nm[target]['tcp'].keys())
        scan_port_keys = nm[target]['tcp'].keys()
        c = {}
        for port in scan_port_keys:
            c[port] = nm[target]['tcp'][port]
        scan_tcp_port_details = c

        content = {
            'command_line': com_line,
            'scan_method': scan_method,
            'host_up_or_down': host_up_or_down,
            'scan_protocol_tcp': scan_protocol_tcp,
            'scan_port_keys': scan_port_keys,
            'scan_tcp_port_details': scan_tcp_port_details
        }

        return content