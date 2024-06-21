from django import forms


class LoginForm(forms.Form):
    iduser = forms.CharField(label='iduser')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')

class FileForm(forms.Form):
    file = forms.FileField(label='file')