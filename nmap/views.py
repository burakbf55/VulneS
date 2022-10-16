from django.shortcuts import render
from .forms import ScannerForm
# Create your views here.


def nmap_scanner(request):
    scanner_form = ScannerForm()
    if request.method == 'POST':
        scanner_form = ScannerForm(request.POST, request.FILES)
        if scanner_form.is_valid():
            scanner_form.save()
            return render(request, 'nmap/nmap-scanner.html', {'scanner_form': scanner_form})
    
    context =  {
    'scanner_form': scanner_form,
    }
    return render(request, 'nmap/nmap-scanner.html', context)