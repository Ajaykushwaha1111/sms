from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from .models import Question
from sms.models import Student
from sms.forms import StudentForm
from django.contrib import messages
def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        username=int(username)
        student =Student.objects.filter(rollno=username,password=password,action=True)
        if student:
            request.session['student_l']=username
            return redirect('startexam')
        else:
            messages.add_message(request, messages.INFO, f'Useranme And Password Wrong !')
            print('username password not match')
    return render(request, 'home.html')

def startexam(request):
    allQuestion =Question.objects.all()
    data ={
        'allQuestion':allQuestion
    }
    return render(request, 'startexam.html', data)

import json
def count_quetion(request):
    res ='no'
    data = json.loads(request.GET.get('data1', ''))
    correct = 0
    attempt =0
    for dd in data:
        attempt = attempt + 1
        q =Question.objects.filter(id=int(dd['id']),correct_answer=dd['opt'])
        if q:
            correct =correct+1


    result = {
            'attempt':attempt,
            'correct':correct,
            'missed':attempt-correct
        }

    if result:
        s =request.session['exam_'] =result
        print(s,"ddddddd")


    return HttpResponse(correct)

def end_exam(request):
    data =request.session.get('exam_')
    return render(request,'endexam.html',data)
from django.core.mail import send_mail

def student_signup(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        email1 =form.cleaned_data.get('email')
        stud =Student.objects.filter(email=email1)
        if stud:
            name =stud[0].name
            pwd =stud[0].password
            roll = stud[0].rollno

            mess =f"""
            Hi, {name} \n
                Your account is activated \n
                Roll : {roll} \n
                Password :{pwd} \n
                
            """
            m = send_mail('Your Account has been activated ',
                          mess,
                          'developerajay1111@gmail.com', [email1],
                      fail_silently=False)
            if m:
                print('mail send')
        messages.add_message(request, messages.INFO, 'Added Customer Successfully !')

        return redirect('home')

    data = {
        'form': form,

    }
    return render(request,'signup.html',data)































# import json
# def count_quetion(request):
#     res=False
#     data = json.loads(request.GET.get('data1', ''))
#     correct = 0
#     attempt =0
#
#     for dd in data:
#         q =Question.objects.filter(id=int(dd['id']),correct_answer=dd['opt'])
#         if q:
#             correct =correct+1
#         attempt = attempt + 1
#
#     result ={
#         'attempt':attempt,
#         'correct':correct,
#         'missed':attempt-correct
#     }
#
#     if result:
#         request.session['exam_result'] = result
#         res =True
#     exam_result =request.session.get('exam_result')
#     print(exam_result)
#
#     return HttpResponse('/')