from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('photo','name','email','mobile','address','aadhar','gender','course')
