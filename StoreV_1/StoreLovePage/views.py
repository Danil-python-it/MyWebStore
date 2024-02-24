from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import Profile_Form, User_LoginForm, User_RegistrationForm, Category_create, ShopItems_create, PictureForShop_create
from .models import Baskets, Profile, Category, ShopItems, PictareForShop


# User_RegistrationForm,  

# MainPage

def MainPage(request):
	Objs = list(reversed(ShopItems.objects.all()))[:12]
	if request.method == "POST":
		shopitems_id = int(list(request.POST)[1])
		basket = Baskets(
			user_id=request.user.id,
			shopitems_id=shopitems_id
		)
		basket.save()
	content = {
		"category":Category.objects.all(),
		"shop_items":Objs,
	}
	return render(request, "FuncPage/MainPage.html", content)

#UserPage
def BasketPage(request):

	user_id = request.user.id
	baskets = Baskets.objects.all().filter(user_id=user_id)
	shop_items = [(ShopItems.objects.get(id=i.shopitems_id))for i in baskets]
	print(shop_items)
	content={
		"status":200,
		"shop_items":shop_items,
	}

	return render(request, "FuncPage/BasketPage.html", content)


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
		form_profile = Profile_Form(request.FILES)
		
		if form.is_valid() and form_profile.is_valid():
			data = {
				"user_name":request.POST["user_name"],
				"user_password":request.POST["user_password"],
				"user_email":request.POST["user_email"],
			}
			user = User.objects.create_user(data["user_name"], data["user_email"], data["user_password"])
			
			if user is not None:
				user.save()
				if len(request.FILES) > 0:
					user_profile = Profile(
						user_id=user.id,
						avatars=request.FILES["avatars"]
					)
					user_profile.save()

				login(request, user)
				return redirect("/user/profile")
			
			else:
				form = User_RegistrationForm(request.POST)
				form_profile = Profile_Form(request.FILES)
				
	else:
		form = User_RegistrationForm()
		form_profile = Profile_Form()


	content = {
		"status":200,
		"form":form,
		"form2":form_profile,

	}

	return render(request, "FuncPage/RegistrationPage.html", content)


def ProfilePage(request):
	if len(Profile.objects.all().filter(user_id=request.user.id)) > 0:
		profile = Profile.objects.get(user_id = request.user.id)
		is_avatars = True
		print("yes")
	else: 
		print("no")
		is_avatars = False
		profile = "None"


	content = {
		"status":200,
		"is_avatars": is_avatars,
		"profile": profile,
	}

	return render(request, "FuncPage/ProfilePage.html", content)


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
	if request.method == "POST":

		basket = Baskets(
			user_id=request.user.id,
			shopitems_id=id
		)
		basket.save()
	content={
		"item":ShopItems.objects.get(id=id),
		"images":PictareForShop.objects.all().filter(shopitems_id=id),
	}
	return render(request,'FuncPage/ShowPage/ShopItemPage.html', content)



#SpecialPage

def NotFindPage(request):

	return render(request, "FuncPage/NotFindPage.html", {"status": 200})

