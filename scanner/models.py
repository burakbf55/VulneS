from django.db import models

from services.models import BaseModel

# Create your models here.


class Nmap(BaseModel): 
    name = models.CharField(max_length=300)
    ip = models.CharField(max_length=200)
    xml_name = models.CharField(max_length=100)
    xml_file = models.FileField(upload_to='nmap/xml/')
    scan_type = models.CharField(max_length=100)
    command_line = models.CharField(max_length=300)
    scan_method = models.CharField(max_length=100,  blank=True, null=True)
    services = models.CharField(max_length=100, blank=True, null=True)
    scan_protocol = models.CharField(max_length=100, blank=True, null=True)
    timestr = models.CharField(max_length=100, blank=True, null=True)
    elapsed = models.CharField(max_length=100, blank=True, null=True)
    uphosts = models.CharField(max_length=100, blank=True, null=True)
    downhosts = models.CharField(max_length=100, blank=True, null=True)
    totalhosts = models.CharField(max_length=100, blank=True, null=True)
    ipv4 = models.CharField(max_length=100, blank=True, null=True)
    vendor = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    tcp_port = models.CharField(max_length=100, blank=True, null=True)
    tcp_port_state = models.CharField(max_length=100, blank=True, null=True)
    tcp_port_reason = models.CharField(max_length=100, blank=True, null=True)
    tcp_port_name = models.CharField(max_length=100, blank=True, null=True)
    tcp_port_product = models.CharField(max_length=100, blank=True, null=True)
    tcp_port_version = models.CharField(max_length=100, blank=True, null=True)
    tcp_port_extrainfo = models.CharField(max_length=100, blank=True, null=True)
    tcp_port_conf = models.CharField(max_length=100, blank=True, null=True)
    tcp_port_cpe = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name