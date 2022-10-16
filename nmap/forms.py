from django import forms
from .models import Nmap

class ScannerForm(forms.ModelForm):

    class Meta:
        model = Nmap
        fields = [
            'name',
            'ip',
            'xml_name',
            'scan_type',
        ]
