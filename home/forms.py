from django import forms
from .models import Help

class ChangePasswordForm(forms.Form):
    old = forms.CharField(max_length=50, label="Old Password",
                          widget=forms.TextInput(attrs={"placeholder": 'Old Password'}))
    new = forms.CharField(max_length=50, label="New Password",
                          widget=forms.TextInput(attrs={"placeholder": 'New Password'}))
    repeat = forms.CharField(max_length=50, label="Repeat Password",
                             widget=forms.TextInput(attrs={"placeholder": 'Repeat Password'}))

    def clean_new(self):
        new = self.cleaned_data.get('new')
        if not len(new) >= 8:
            raise forms.ValidationError("Password Must Be 8 Charector!")
        return new

    def clean_repeat(self):
        new = self.cleaned_data.get('new')
        repeat = self.cleaned_data.get('repeat')
        if not new == repeat:
            raise forms.ValidationError("Old Password And New Password Not Match!")
        return repeat


class ForgetPasswordForm(forms.Form):
    rollno = forms.IntegerField(label='Roll No', widget=forms.TextInput(attrs={'placeholder': 'Enter Roll No...'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter Email...'}))


class HelpForm(forms.ModelForm):
    class Meta:
        model = Help
        fields = '__all__'

    message = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}))
