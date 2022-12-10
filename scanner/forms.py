from django import forms

from .models import Nmap


class ScannerForm(forms.ModelForm):

    class Meta:
        model = Nmap
        fields = [
            'name',
            'ip',
            'ports',
            'xml_name',
            'arguments',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a scan name'}),
            'ip': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a target ip'}),
            'ports': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a port range; -p 1-1024, --top-ports 100 etc. '}),
            'xml_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a xml file name without .xml ex: scan1xmlname'}),
            'arguments': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter a nmap arguments; -sV, -sC, -A etc. '}),
        }
