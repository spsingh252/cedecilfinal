

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import student
# Create your views here.


def new_admisson(request):
    if request.method=='POST':
        student_name=request.POST['student_name']
        email_id=request.POST['email_id']
        age=request.POST['age']

        student_obj=student(student_name=student_name,email_id=email_id,age=age)
        student_obj.save()
        return render(request, 'admisson_form.html')
    else:
        return render(request, 'admisson_form.html')


def listed_student(request):
    studentdetails_obj=student.objects.all()
    return render(request, 'studentlist.html',{'studentlist':studentdetails_obj})