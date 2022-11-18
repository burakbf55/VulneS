from django.db import models

from services.models import BaseModel

# Create your models here.


class Nmap(BaseModel): 
    # get form data
    name = models.CharField(max_length=300)
    ip = models.CharField(max_length=200)
    xml_name = models.CharField(max_length=100, blank= True, null= True)
    xml_file = models.FileField(upload_to='nmap/xml/', blank= True, null= True)
    scan_type = models.CharField(max_length=100)
    # get scan data
    command_line = models.CharField(max_length=300, blank=True, null=True) # nm.scaninfo() get method.
    scan_method = models.CharField(max_length=100,  blank=True, null=True)
    host_up_or_down = models.CharField(max_length=100,  blank=True, null=True) # nm['127.0.0.1'].state()
    scan_protocol_tcp = models.CharField(max_length=100,  blank=True, null=True) # nm['127.0.0.1'].all_protocols()
    scan_port_keys = models.CharField(max_length=100,  blank=True, null=True) # nm['127.0.0.1']['tcp'].keys()
    scan_tcp_port_details = models.CharField(max_length=100,  blank=True, null=True) # nm['127.0.0.1']['tcp'][22]
                                                                                     # or nm['127.0.0.1'].tcp(22)


    def __str__(self):
        return self.name