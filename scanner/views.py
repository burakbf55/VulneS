from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from services.services import NmapService

from .forms import ScannerForm
from .models import Nmap

# Create your views here.


def nmap_scanner(request):
    scanner_form = ScannerForm()
    if request.method == 'POST':
        scanner_form = ScannerForm(request.POST, request.FILES)
        if scanner_form.is_valid():
            target = scanner_form.cleaned_data['ip']
            scan_type = scanner_form.cleaned_data['scan_type']
            result = NmapService.nmap(target,'22',scan_type)
            n_m = Nmap()
            # get form data
            n_m.name = scanner_form.cleaned_data['name']
            n_m.ip = target
            n_m.xml_name = scanner_form.cleaned_data['xml_name']
            n_m.scan_type = scan_type
            # get scan data 
            n_m.command_line = result['command_line']
            n_m.scan_method = result['scan_method']
            n_m.host_up_or_down = result['host_up_or_down']
            n_m.scan_protocol_tcp = result['scan_protocol_tcp']
            n_m.scan_port_keys = result['scan_port_keys']
            n_m.scan_tcp_port_details = result['scan_tcp_port_details']
            n_m.save()
        
            context =  {
            'scanner_form': scanner_form,
            }
            return redirect('vulnerability_scanner')
        else:
            return HttpResponse("Your form is wrong, reload on")
    else:
        scanner_form = ScannerForm()
    
    nmap_model = Nmap.objects.all().order_by("-id")
    context =  {
    'scanner_form': scanner_form,
    'nmap_model': nmap_model
    }    

    return render(request, 'index.html', context)


def nmap_detail(request, id):
    nmap_model = Nmap.objects.all().filter(id=id)
    
    context = {
        'nmap_model': nmap_model
    }

    return render(request, 'result.html', context)