from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
	return HttpResponse("Hello world!")
	#return render(request, 'home.html')
