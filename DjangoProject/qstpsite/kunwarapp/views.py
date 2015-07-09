from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
	return render(request,"kunwar/homepage.html")
def Page1(request):
	return render(request,"kunwar/page1.html")
def Page2(request):
	return render(request,"kunwar/page2.html")
# Create your views here.