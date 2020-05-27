from django.shortcuts import render, HttpResponse, redirect
import json
from django.core.mail import send_mail
# Create your views here.
from .models import Question, Course
from sms.models import Student
from sms.forms import StudentForm
from django.contrib import messages
from cms.utility import track


def home(request):
    if request.session.get('student_l'):
        return redirect('dashboard')
    data = {
        'current_path': request.get_full_path()
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        username = int(username)
        student = Student.objects.filter(rollno=username, password=password, action=True)
        if student:
            track.track_location(request, student)
            request.session['student_l'] = username
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.INFO, f'Useranme And Password Wrong !')
            print('username password not match')
    return render(request, 'home.html', data)


def startexam(request):
    data = dict()
    if not request.session.get('student_l'):
        return redirect('home')
    if request.method == "POST":
        selectCourse = request.POST.get('selectCourse')
        student_l = request.session.get('student_l')
        one_student = Student.objects.get(rollno=student_l)
        oneC = Course.objects.get(id=selectCourse)
        allQuestion = Question.objects.filter(course=oneC).order_by('-id')[:15]
        data = {
            'allQuestion': allQuestion,
            'one_student': one_student
        }
    return render(request, 'startexam.html', data)


def count_quetion(request):
    res = 'no'
    data = json.loads(request.GET.get('data1', ''))
    correct = 0
    attempt = 0
    for dd in data:
        attempt = attempt + 1
        q = Question.objects.filter(id=int(dd['id']), correct_answer=dd['opt'])
        if q:
            correct = correct + 1

    result = {
        'attempt': attempt,
        'correct': correct,
        'wrong': attempt - correct,
        'missed': 15 - attempt
    }

    if result:
        s = request.session['exam_'] = result
        print(s, "ddddddd")

    return HttpResponse(correct)


def end_exam(request):
    if not request.session.get('student_l'):
        return redirect('home')
    data = request.session.get('exam_')

    result =round(data['correct']*100/15)
    myresult = dict()
    myresult['percentage'] = result
    if result <= 33:
        myresult['status'] = 'Fail'
    if result >= 33 and result < 50:
        myresult['status'] = 'Third'
    if result >= 50 and result < 60:
        myresult['status'] = 'Second'
    if result >= 60 and result < 70:
        myresult['status'] = 'First'
    if result >= 80 and result < 90:
        myresult['status'] = 'Great'
    if result >= 90 and result <= 100:
        myresult['status'] = 'Exellent'

    data['myresult']=myresult
    print(data)
    return render(request, 'endexam.html', data)


def student_signup(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        email1 = form.cleaned_data.get('email')
        stud = Student.objects.filter(email=email1)
        if stud:
            track.track_location(request, stud)
            name = stud[0].name
            pwd = stud[0].password
            roll = stud[0].rollno

            mess = f"""
Hi, {name} \n
Your account is activated \n
Roll : {roll} \n
Password :{pwd} \n

            """
            try:
                m = send_mail('Your Account has been activated ',
                              mess,
                              'developerajay1111@gmail.com', [email1],
                              fail_silently=False)
                if m:
                    messages.add_message(request, messages.INFO, f'Check Your Mail {email1} For access details !')

            except:
                messages.add_message(request, messages.INFO, f'Your Mail Correct {email1} For access details !')
                s = Student.objects.last()
                s.delete()
        messages.add_message(request, messages.INFO, 'Added Customer Successfully !')
        return redirect('home')

    data = {
        'form': form,

    }
    return render(request, 'signup.html', data)


def logout_student(request):
    if not request.session.get('student_l'):
        return redirect('home')
    del request.session['student_l']
    return redirect('home')


def dashboard_student(request):
    if not request.session.get('student_l'):
        return redirect('home')
    courses = Course.objects.all()
    rollno = request.session.get('student_l')
    one_student = Student.objects.filter(rollno=rollno)
    data = {
        'courses': courses,
        'one_student': one_student[0],
    }
    return render(request, 'sdashbord.html', data)


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
from .forms import HelpForm, ChangePasswordForm, ForgetPasswordForm

from .models import Help


def help(request):
    form = HelpForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        mobile = form.cleaned_data.get('mobile')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        print(name, email, mobile, message)
        help1 = Help.objects.create(name=name, mobile=mobile, email=email, message=message)
        if help1:
            messages.add_message(request, messages.INFO, 'Your Request Send Successfully !')

    data = {
        'form': form
    }

    return render(request, 'help.html', data)


def forget_password(request):
    form = ForgetPasswordForm(request.POST or None)
    if form.is_valid():
        roll = form.cleaned_data.get('rollno')
        email = form.cleaned_data.get('email')
        print(roll, email)
        stud = Student.objects.filter(rollno=roll, email=email)
        if stud:
            name = stud[0].name
            pwd = stud[0].password
            roll = stud[0].rollno
            mess = f"""
            Hi, {name} \n
            Your old Password Details \n
            Roll : {roll} \n
            Password :{pwd} \n

            """
            try:
                m = send_mail('Your Password Details',
                              mess,
                              'developerajay1111@gmail.com', [email],
                              fail_silently=False)
                if m:
                    messages.add_message(request, messages.INFO, f'Check Your Mail {email} I have send Password !')

            except:
                messages.add_message(request, messages.INFO, f'Internet Connection Failed !')
        else:
            messages.add_message(request, messages.INFO, 'Your Roll No and Email no Match !')
    data = {
        'form': form
    }
    return render(request, 'forget_password.html', data)


def change_password(request):
    if not request.session.get('student_l'):
        return redirect('home')
    form = ChangePasswordForm(request.POST or None)
    if form.is_valid():
        old = form.cleaned_data.get('old')
        new = form.cleaned_data.get('new')
        repeat = form.cleaned_data.get('repeat')
        print(old, new, repeat)
        roll = request.session.get('student_l')
        sm = Student.objects.filter(rollno=roll, password=old)
        if sm:
            Student.objects.filter(rollno=roll, password=old).update(password=new)
            print('password change')
            messages.add_message(request, messages.INFO, 'Your Password Changed !')
        else:
            messages.add_message(request, messages.INFO, 'Old Password not Match !')

    data = {
        'form': form
    }
    return render(request, 'change_password.html', data)
