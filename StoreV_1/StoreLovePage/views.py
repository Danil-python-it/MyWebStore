from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import User_LoginForm


# Create your views here.
def MainPage(request):
	context={
		"status":200,
	}
	return render(request, "FuncPage/MainPage.html", context)


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


def ProfilePage(request):
	pass










def NotFindPage(request):

	return render(request, "FuncPage/NotFindPage.html", {"status": 200})

