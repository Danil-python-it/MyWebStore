from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import User_LoginForm, User_RegistrationForm, Category_create, ShopItems_create, PictureForShop_create
from .models import Category, ShopItems, PictareForShop


# User_RegistrationForm,  

# MainPage

def MainPage(request):
	context={
		"status":200,
	}
	return render(request, "FuncPage/MainPage.html", context)


#UserPage
def LoginPage(request):
	if request.user.is_authenticated == True: return redirect("/user/profile")

	if request.method == "POST":
		form = User_LoginForm(request.POST)
		if form.is_valid():
			data = {
				"user_name":request.POST["user_name"],
				"user_password":request.POST["user_password"],
			}
			
			user = authenticate(request, username=data["user_name"], password=data["user_password"])
			if user is not None:
				login(request, user)
				print("it's ok")
				return redirect("/user/profile")
			else:
				print("warning!!!")
				form = User_LoginForm(request.POST)
	
	else:
		form = User_LoginForm()
	
	context={
		"status":200,
		"form":form,
	}
	
	return render(request, "FuncPage/LoginPage.html", context)


def LogoutPage(request):
	logout(request)
	return redirect('/')


def RegistionPage(request):
	if request.user.is_authenticated == True: return redirect("/user/profile")

	if request.method == "POST":
		form = User_RegistrationForm(request.POST)
		if form.is_valid():
			data = {
				"user_name":request.POST["user_name"],
				"user_password":request.POST["user_password"],
				"user_email":request.POST["user_email"],
			}
			
			user = User.objects.create_user(data["user_name"], data["user_email"], data["user_password"])
			if user is not None:
				user.save()
				login(request, user)
				print("it's ok")
				return redirect("/user/profile")
			else:
				print("warning!!!")
				form = User_RegistrationForm(request.POST)
	
	else:
		form = User_RegistrationForm()

	content = {
		"status":200,
		"form":form,
	}

	return render(request, "FuncPage/RegistrationPage.html", content)


def ProfilePage(request):

	return render(request, "FuncPage/ProfilePage.html", {"status":200})


#MainContent

def ShopPage(request):
	content = {
		"category":Category.objects.all()
	}
	return render(request, "FuncPage/ShopPage.html", content)


def CategoryCreatePage(request):
	if request.user.is_superuser == False: return redirect("/shop/list")

	if request.method == "POST":
		form = Category_create(request.POST,request.FILES)
		
		if form.is_valid():
			form.save()
			return redirect("/shop/list")
		else:
			print("warning")
			print(request)
			print(request.POST)
			print(request.FILES)
			

	else:
		form = Category_create()

	content = {
		"status":200,
		"form":form,
	}

	return render(request, "FuncPage/CreateModels/Category.html", content)









#SpecialPage

def NotFindPage(request):

	return render(request, "FuncPage/NotFindPage.html", {"status": 200})

