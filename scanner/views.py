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
    nmap_model = Nmap.objects.all().filter(id=id)

    context = {
        'nmap_model': nmap_model,
    }

    return render(request, 'result.html', context)