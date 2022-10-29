from django.shortcuts import render

# Create your views here.

# pages

def contact(request):
    return render(request, 'contact-us.html', {})
