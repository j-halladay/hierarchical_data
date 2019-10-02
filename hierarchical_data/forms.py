from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class AddFile(forms.Form):

    name = forms.CharField(max_length=50)
    file_link = forms.CharField(max_length=400)


class AddFolder(forms.Form):

    name = forms.CharField(max_length=50)
