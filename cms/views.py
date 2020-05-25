from django.shortcuts import render,redirect
from django.contrib import messages
from sms.forms import StudentForm
from sms.models import Student
from django.contrib.auth import authenticate,login,logout
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user =authenticate(username=username,password=password)

        if user:
            print('login')
            login(request,user)
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, f'Useranme And Password Wrong !')
            print('username password not match')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login_u')