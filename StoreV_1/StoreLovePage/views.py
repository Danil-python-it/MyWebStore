from django.shortcuts import render

# Create your views here.
def NotFindPage(request):

	return render(request, "NotFindPage.html", {"status": 200})

