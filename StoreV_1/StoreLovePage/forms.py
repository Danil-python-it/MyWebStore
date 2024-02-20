from django import forms

class User_LoginForm(forms.Form):
	user_name = forms.CharField(label="Имя", max_length=100)
	user_password = forms.CharField(label="Пароль", max_length=100)
