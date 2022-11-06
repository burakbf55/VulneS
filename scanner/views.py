from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from services.services import NmapService
from .forms import ScannerForm

# Create your views here.


def nmap_scanner(request):
    scanner_form = ScannerForm()
    if request.method == 'POST':
        scanner_form = ScannerForm(request.POST, request.FILES)
        if scanner_form.is_valid():
            scanner_form.save()
            target = scanner_form.cleaned_data['ip']
            print(NmapService.nmap(target, '22'))
            context =  {
            'scanner_form': scanner_form,
            }
            messages.success(request, "Scan added successfully")
            return redirect('vulnerability_scanner')
        else:
            return HttpResponse("Your form is wrong, reload on")
    else:
        scanner_form = ScannerForm()

    context =  {
    'scanner_form': scanner_form,
    }    

    return render(request, 'index.html', context)