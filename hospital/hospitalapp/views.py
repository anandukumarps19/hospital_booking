from django.http import HttpResponse
from django.shortcuts import render

from .forms import Bookingform
from .models import Department, Doctors


def Home(request):
    # person = {
    #     'name': 'Anand',
    #     'age': 27,
    #     'Place':'Kottayam'
    # }
    numbers ={
        'num1': 10,
    }
    return render(request,'Home.html', numbers)

def about(request):
    number = {
        'num1':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,'about.html',number)

def booking(request):
    if request.method=='POST':
        form = Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = Bookingform()
    dict_form ={
        'form':form
    }
    return render(request,"booking.html", dict_form)

def doctors(request):
    dict_doct = {
        'doct': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doct)

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,'department.html',dict_dept)