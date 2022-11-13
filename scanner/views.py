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
            scanner_form.save()
            target = scanner_form.cleaned_data['ip']
            scan_type = scanner_form.cleaned_data['scan_type']
            result = NmapService.nmap(target,'22',scan_type)
            n_m = Nmap()
            n_m.name = scanner_form.cleaned_data['name']
            n_m.ip = scanner_form.cleaned_data['ip']
            n_m.xml_name = scanner_form.cleaned_data['xml_name']
            n_m.command_line = result['nmap']['command_line']
            n_m.scan_method = result['nmap']['scaninfo']['tcp']['method']
            n_m.timestr = result['nmap']['scanstats']['timestr']
            n_m.elapsed = result['nmap']['scanstats']['elapsed']
            n_m.uphosts = result['nmap']['scanstats']['uphosts']
            n_m.downhosts = result['nmap']['scanstats']['downhosts']
            n_m.totalhosts = result['nmap']['scanstats']['totalhosts']
            n_m.ipv4 = result['scan'][f'{target}']['addresses']['ipv4']
            n_m.vendor = result['scan'][f'{target}']['vendor']
            n_m.state = result['scan'][f'{target}']['status']['state']
            n_m.reason = result['scan'][f'{target}']['status']['reason']
            n_m.tcp_port = result['nmap']['scaninfo']['tcp']['services']
            n_m.tcp_port_state = result['scan'][f'{target}']['tcp'][22]['state']
            n_m.tcp_port_reason = result['scan'][f'{target}']['tcp'][22]['reason']
            n_m.tcp_port_name = result['scan'][f'{target}']['tcp'][22]['name']
            n_m.tcp_port_product = result['scan'][f'{target}']['tcp'][22]['product']
            n_m.tcp_port_version = result['scan'][f'{target}']['tcp'][22]['version']
            n_m.tcp_port_extrainfo = result['scan'][f'{target}']['tcp'][22]['extrainfo']
            n_m.tcp_port_conf = result['scan'][f'{target}']['tcp'][22]['conf']
            n_m.tcp_port_cpe = result['scan'][f'{target}']['tcp'][22]['cpe']
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


def nmap_detail(request):

    context = {

    }

    return render(request, 'result.html', context)