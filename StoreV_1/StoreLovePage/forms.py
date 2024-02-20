from django import forms

class User_LoginForm(forms.Form):

	user_name = forms.CharField(
		label="Имя",
		max_length=100,
		widget=forms.TextInput(attrs={
				"class":"form-control",
				"id":"username",
			}
		)
	)

	user_password = forms.CharField(
		widget=forms.PasswordInput(attrs={
				"class":"form-control",
				"id":"userpassword",
			}
		),
		label="Пароль", 
		max_length=100,
	)


class User_RegistrationForm(forms.Form):

	user_name = forms.CharField(
		widget=forms.TextInput(attrs={
				"class":"form-control",
				"id":"username",
			}
		),
		label="Имя", 
		max_length=100,
		min_length=3,
	)

	user_password = forms.CharField(
		widget=forms.PasswordInput(attrs={
				"class":"form-control",
				"id":"userpassword",
			}
		), 
		label="Пароль", 
		max_length=100, 
		min_length=8,
	)

	user_email = forms.EmailField(
		widget=forms.EmailInput(attrs={
				"class":"form-control",
				"id":"useremail",
			}
		),
		label="Почта", 
		max_length=100,
	)