from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *


# Create your views here.
def student(request):
    SFEO=StudentForm()
    d={'SFEO':SFEO}
    if(request.method=='POST'):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            Sname=SFDO.cleaned_data['Sname']
            Sage=SFDO.cleaned_data['Sage']
            Sid=SFDO.cleaned_data['Sid']
            Semail=SFDO.cleaned_data['Semail']
            Remail=SFDO.cleaned_data['Remail']
            SO=Student.objects.get_or_create(Sname=Sname,Sage=Sage,Sid=Sid,Semail=Semail)[0]
            SO.save()

        #Student.objects.filter(Sname='kavitha').update(Semail='kavi@gmail.com')
            Student.objects.filter(Sname='kavitha').delete()
            QSO=Student.objects.all()
            d1={'QSO':QSO}
            return render(request,'display_student.html',d1)
        else:
            return HttpResponse('invalid data')

    return render(request,'student.html',d)

