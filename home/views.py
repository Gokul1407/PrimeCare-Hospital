from django.shortcuts import render
from appointments.models import Departments
# Create your views here.



# Create your views here.

def homepage(request):
    
    return render(request, 'index.html')

def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')