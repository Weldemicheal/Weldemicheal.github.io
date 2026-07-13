from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'roofing/home.html')

def about(request):
    return render(request, 'roofing/about.html')

def services(request):
    return render(request, 'roofing/services.html')

def contact(request):
    if request.method == 'POST':
        return render(request, 'roofing/contact.html', {'form_submitted': True})
    return render(request, 'roofing/contact.html')
