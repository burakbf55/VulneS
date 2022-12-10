from django.db import models

from services.models import BaseModel

# Create your models here.


class Nmap(BaseModel): 
    # get form data
    name = models.CharField(max_length=300)
    ip = models.CharField(max_length=200)
    ports = models.CharField(max_length=200)
    xml_name = models.CharField(max_length=100, blank= True, null= True)
    xml_file = models.FileField(upload_to='nmap/xml/', blank= True, null= True)
    arguments = models.CharField(max_length=100, blank= True, null= True)
    # get scan data
    output = models.TextField(blank= True, null= True)


    def __str__(self):
        return self.name