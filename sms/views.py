from django.shortcuts import render,redirect
from django.contrib import messages
from sms.forms import StudentForm
from sms.models import Student

def details(request):
    if not request.user.is_authenticated:
        return redirect('login_u')
    all_students =Student.objects.all()
    data ={
        'all_rec':all_students
    }

    return render(request,'details.html',data)


def addCustomer(request):
    if not request.user.is_authenticated:
        return redirect('login_u')
    form =StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Added Customer Successfully !')
        return redirect('details')

    data={
        'form':form,

    }
    return render(request,'addc.html',data)


def editCustomer(request,id=None,slug=None):
    if not request.user.is_authenticated:
        return redirect('login_u')

    stu =Student.objects.get(id=id)
    form = StudentForm(request.POST or None, request.FILES or None,instance=stu)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, f'{stu}, Edited Successfully !')
        return  redirect('details')
    data = {
        'form': form
    }

    return render(request,'addc.html',data)

def deleteCustomer(request,slug=None,id=None):
    if not request.user.is_authenticated:
        return redirect('login_u')
    stu = Student.objects.get(id=id)
    if request.method=='POST':
        stu.delete()
        return redirect('details')
    return render(request,'delete.html',{'stu':stu})

def viewCustomer(request,id=None,slug=None):
    if not request.user.is_authenticated:
        return redirect('login_u')
    one_student = Student.objects.get(id=id)
    return render(request,'viewCustomer.html',{'one_student':one_student})



