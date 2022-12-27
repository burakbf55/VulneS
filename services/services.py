import json
import os
import xml.etree.ElementTree as ElementTree

import xmltodict

from .views import nmap_to_command


class NmapService():
    def __init__(self, target, ports, arguments, filename):
        self.target = target
        self.ports = ports
        self.arguments = arguments
        self.filename = filename
        # ileride kullanılacak.

    def parse_nmap_xml(xml):
        tree = ElementTree.parse("/code/media/xml/" + xml + ".xml")
        root = tree.getroot()
        parsed_data = []
        
        for host in root.findall('host'):
            # updown=host.find('status').get('state')
            for address in host.findall('address'):
                curr_address = address.attrib['addr']
                data = {
                    'command_line': curr_address, 
                    'address': curr_address,
                    'ports-2': []
                }
                states = host.findall('ports/extraports/state')
                ports = host.findall('ports/port')
                state = host.findall('ports/port/state')
                for i in range(len(ports)):
                    # if states[i].attrib['state'] == 'closed':
                    #     continue 
                    port_id = ports[i].attrib['portid']
                    protocol = ports[i].attrib['protocol']
                    services = ports[i].findall('service')
                    state = ports[i].find('state').attrib['state']
                    cpe_list = []
                    service_name = ""
                    service_product = ""
                    service_version = ""
                    for service in services:
                        for key in ['name', 'product', 'version']:
                            if key in service.attrib:
                                if key == 'name':
                                    service_name = service.attrib['name']
                                elif key == 'product':
                                    service_product = service.attrib['product']
                                elif key == 'version':
                                    service_version = service.attrib['version']
                        cpes = service.findall('cpe')
                        for cpe in cpes:
                            cpe_list.append(cpe.text)
                        data['ports-2'].append({
                            'port_id': port_id,
                            'status': state,
                            'protocol': protocol,
                            'service_name': service_name,
                            'service_product': service_product,
                            'service_version': service_version,
                            'cpes': cpe_list
                        })
                        parsed_data.append(data)
        return parsed_data
    
    def count_ports(parsed_data):
        open_count = 0
        filtered_count = 0
        closed_count = 0
        
        for host in parsed_data:
            for port in host['ports-2']:
                if port['status'] == 'open':
                    open_count += 1
                elif port['status'] == 'filtered':
                    filtered_count += 1
                elif port['status'] == 'closed':
                    closed_count += 1
        
        return open_count, filtered_count, closed_count

    def nmap_xml_to_json(filename):
        with open("/code/media/xml/" + filename + ".xml") as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            json_data = json.dumps(data_dict)
            return json_data

    def nmap(target, ports, arguments ,filename):
        nmap_to_command(target, filename, ports, arguments)
        
        return NmapService.parse_nmap_xml(filename)
        