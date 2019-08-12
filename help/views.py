from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('hello')

def articles(request):
	return HttpResponse('articles')

def article_details(request, pk):
	return HttpResponse("hello" + str(pk))
# Create your views here.
