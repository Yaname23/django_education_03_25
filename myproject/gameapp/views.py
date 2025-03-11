from random import choice, random, randint

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello Word!')

def orel_reshka(request):
    return HttpResponse(choice(['Орел',  'Решка']))

def kub(request):
    return HttpResponse(str(randint(1, 7)))

def numbers(request):
    return HttpResponse(str(randint(0, 100)))

def home_page(request):
    context = {

    }
    return render(request, 'gameapp/home.html', context=context)

def about_me(request):
    context = {

    }
    return render(request, 'gameapp/about-me.html', context=context)





