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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ip': forms.TextInput(attrs={'class': 'form-control'}),
            'xml_name': forms.TextInput(attrs={'class': 'form-control'}),
            'scan_type': forms.TextInput(attrs={'class': 'form-control'}),
        }
