from django import forms
from .models import Category, ShopItems, PictareForShop


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


class Category_create(forms.ModelForm):
	class Meta:
		model = Category
		fields = [ 'title', 'description', 'icon' ]
		widgets = {
			'title': forms.TextInput(attrs={
				'class':'"form-control"'
			}),
			'description': forms.TextInput(attrs={
				'class':'"form-control"'
			}),
		}
		labels = {
			'title':"Название",
			'description':"Описание",
			'icon':"Главная картинка",
		}
	
		

class ShopItems_create(forms.ModelForm):
	class Meta:
		model = ShopItems
		fields = [
			'title', 'description', 'currency', 'price', 'icon'
		]
		widgets = {
			'title': forms.TextInput(attrs={
				'class':'"form-control"'
			}),
			'description': forms.TextInput(attrs={
				'class':'"form-control"'
			}),
			'currency': forms.TextInput(attrs={
				'class':'"form-control"'
			}),
		}

		labels = {
			'title':"Название",
			'description':"Описание",
			'currency':"Валюта",
			'price':"Цена",
			'icon':"Главная картинка",
		}


class PictureForShop_create(forms.ModelForm):
	class Meta:
		model = PictareForShop
		fields = ['picture']
		labels = {'picture':"Изображение"}
			