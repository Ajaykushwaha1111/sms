from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    address=forms.CharField(widget=forms.Textarea(attrs={
                                                         'rows':'2'
                                                         }))