from django import forms


class LoginForm(forms.Form):
    iduser = forms.CharField(label='iduser')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')

class FileForm(forms.Form):
    file = forms.FileField(label='file')

class SearchForm(forms.Form):
    idlibro = forms.CharField(label='idlibro')

class CantidadForm(forms.Form):
    cantidad = forms.IntegerField(label='cantidad')