from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import User_LoginForm, User_RegistrationForm, Category_create, ShopItems_create, PictureForShop_create
from .models import Category, ShopItems, PictareForShop


# User_RegistrationForm,  

# MainPage

def MainPage(request):
	Objs = list(reversed(ShopItems.objects.all()))
	content = {
		"category":Category.objects.all(),
		"shop_items":Objs[:12],
	}
	return render(request, "FuncPage/MainPage.html", content)

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
				return redirect("/user/profile")
			else:
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
				return redirect("/user/profile")
			else:
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
def CategoryCreatePage(request):
	if request.user.is_superuser == False: return redirect("/")

	if request.method == "POST":
		form = Category_create(request.POST,request.FILES)

		if form.is_valid():
			form.save()
			return redirect("/")
		
	else:
		form = Category_create()

	content = {
		"status":200,
		"form":form,
	}

	return render(request, "FuncPage/CreateModels/Category.html", content)

def ShopItemsCreatePage(request):
	if request.user.is_superuser == False: return redirect("/")

	if request.method == "POST":
		form = ShopItems_create(request.POST,request.FILES)
		images_input = PictureForShop_create(request.FILES)

		if form.is_valid() and images_input.is_valid():
			print()
			Obj = ShopItems(
				title=request.POST["title"],
				description=request.POST["description"],
				price=int(request.POST["price"]),
				currency=request.POST["currency"],
				category_id=int(request.POST["category"]),
				icon=request.FILES["icon"],
			)
			Obj.save()
			images_input = dict(request.FILES)["picture"]

			for index in range(0,len(images_input)):
				image = PictareForShop(
					picture=images_input[index],
					shopitems_id=Obj.id
				)
				image.save()
			
			return redirect("/")
				
	else:
		form = ShopItems_create()
		images_input = PictureForShop_create()

	content = {
		"status":200,
		"form":form,
		"images_input":images_input,
	}

	return render(request, "FuncPage/CreateModels/ShopItems.html", content)

def CategoryPage(request,id):
	print(id)
	content={
		"category":Category.objects.get(id=id),
		"shop_items":ShopItems.objects.all().filter(category_id=id)
		
	}
	return render(request,'FuncPage/ShowPage/CategoryPage.html', content)
	

def ShopItemPage(request,id):
	print(id)
	content={
		"item":ShopItems.objects.get(id=id),
		"images":PictareForShop.objects.all().filter(shopitems_id=id),
	}
	return render(request,'FuncPage/ShowPage/ShopItemPage.html', content)



#SpecialPage

def NotFindPage(request):

	return render(request, "FuncPage/NotFindPage.html", {"status": 200})

