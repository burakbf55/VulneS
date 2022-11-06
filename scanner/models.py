from django.db import models
from services.models import BaseModel
# Create your models here.


class Nmap(BaseModel): 
    name = models.CharField(max_length=300)
    ip = models.CharField(max_length=200)
    xml_name = models.CharField(max_length=100)
    xml_file = models.FileField(upload_to='nmap/xml/')
    scan_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name