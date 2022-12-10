import json
import os

import xmltodict

from .views import nmap_to_command


class NmapService():
    def __init__(self, target, ports, arguments, filename):
        self.target = target
        self.ports = ports
        self.arguments = arguments
        self.filename = filename
        # ileride kullanılacak.

    def nmap_xml_to_json(filename):
        with open("/code/media/xml/" + filename + ".xml") as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            json_data = json.dumps(data_dict)
            return json_data

    def nmap(target, ports, arguments ,filename):
        nmap_to_command(target, filename, ports, arguments)
        
        return NmapService.nmap_xml_to_json(filename)
        