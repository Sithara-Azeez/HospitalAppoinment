from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Departments, Doctors
from .forms import *

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    context = {
        'form':form
    }
    return render(request, 'booking.html', context)

def doctors(request):
    context = {
        'doctors':Doctors.objects.all()
    }
    return render(request, 'doctors.html', context)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    context = {
        'dept':Departments.objects.all()
    }
    return render(request, 'department.html', context)