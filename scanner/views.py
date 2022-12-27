from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from services.services import NmapService

from .forms import ScannerForm
from .models import Nmap

# Create your views here.

def save_nm_db(name,ip,ports,xml_name,arguments,output):
    nm = Nmap()
    nm.name = name
    nm.ip = ip
    nm.ports = ports
    nm.xml_name = xml_name
    nm.arguments = arguments
    nm.output = output
    nm.save()
    return nm

def nmap_scanner(request):
    scanner_form = ScannerForm()
    if request.method == 'POST':
        scanner_form = ScannerForm(request.POST, request.FILES)
        if scanner_form.is_valid():
            context = {}
            name = scanner_form.cleaned_data['name']
            target = scanner_form.cleaned_data['ip']
            ports = scanner_form.cleaned_data['ports']
            arguments = scanner_form.cleaned_data['arguments']
            xml_name = scanner_form.cleaned_data['xml_name']
            result = NmapService.nmap(target, ports, arguments, xml_name)
            save_nm_db(name, target, ports, xml_name, arguments, result)
            print(result)
            
            context =  {
            'scanner_form': scanner_form,
            'result': result
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
    nmap_model = Nmap.objects.get(id=id)
    xml_name = nmap_model.xml_name
    context = {
        'ports2': []
    }

    result = NmapService.parse_nmap_xml(xml_name)
    open_count, filtered_count, closed_count = NmapService.count_ports(result)
    for raw_data in result:
        print(raw_data)
        adress = raw_data['address']
        ports = raw_data['ports-2']
        for port_data in ports:
            print(port_data)
            context['ports2'].append(port_data)
            context['ip'] = adress
            context['protocol'] = port_data['protocol']
            context['port'] = port_data['port_id']
            context['service'] = f"{port_data['service_name'] if port_data['service_name'] else ''} {port_data['service_product'] if port_data['service_product'] else ''} {port_data['service_version'] if port_data['service_version'] else ''}"
    context['nmap_model'] = nmap_model
    context['open_count'] = open_count
    context['filtered_count'] = filtered_count
    context['closed_count'] = closed_count
    context['xml_name'] = xml_name


    return render(request, 'result.html', context)