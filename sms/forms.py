from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('photo','name','email','mobile','address','gender','course')

    address=forms.CharField(widget=forms.Textarea(attrs={'rows':'4'}))
    mobile=forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'return isMobileOnly(event);'}))