from django.shortcuts import render

# Create your views here.
def MainPage(request):
	context={
		"status":200,
	}

	return render(request, "MainPage.html", context)














def NotFindPage(request):

	return render(request, "NotFindPage.html", {"status": 200})

