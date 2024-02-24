from django import forms
from .models import Profile ,Category, ShopItems


	

class Profile_Form(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['avatars']
		labels = {
			'avatars':"Фото аккаунта",
		}



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
		fields = [ 'title', 'description']
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
		}
	
		



CHOICES_category = [ (category.id, category.title) for category in Category.objects.all() ]		

class ShopItems_create(forms.ModelForm):
	category =  forms.ChoiceField(choices=CHOICES_category)
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




class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PictureForShop_create(forms.Form):
	picture = MultipleFileField()

