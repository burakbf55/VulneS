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
        tags = [elem.tag for elem in root.iter()]       
        print(tags)

        nmap_args = root.attrib['args']
        for host in root.findall('host'):
            for address in host.findall('address'):
                curr_address = address.attrib['addr']
                data = {
                    'address': curr_address,
                    'ports': []
                }
                states = host.findall('ports/port/state')
                ports = host.findall('ports/port')
                for i in range(len(ports)):
                    if states[i].attrib['state'] == 'closed':
                        continue  # Skip closed ports
                    port_id = ports[i].attrib['portid']
                    protocol = ports[i].attrib['protocol']
                    services = ports[i].findall('service')
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
                        data['ports'].append({
                            'port_id': port_id,
                            'protocol': protocol,
                            'service_name': service_name,
                            'service_product': service_product,
                            'service_version': service_version,
                            'cpes': cpe_list
                        })
                        parsed_data.append(data)
        return nmap_args, parsed_data

    def nmap_xml_to_json(filename):
        with open("/code/media/xml/" + filename + ".xml") as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            json_data = json.dumps(data_dict)
            return json_data

    def nmap(target, ports, arguments ,filename):
        nmap_to_command(target, filename, ports, arguments)
        
        return NmapService.parse_nmap_xml(filename)
        