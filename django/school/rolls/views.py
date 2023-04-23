from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import*
from django.http import JsonResponse


def index(request):
    return render(request, 'pages/mainPage.html')


def search(request):
    
    return render(request, 'pages/search.html')


def searchResult(request):
    s=Student.objects.all()
    title=None
    if 'box' in request.GET:
        box = request.GET['box']
        if box:
            s=s.filter(title__icontains=box)


    context={ 'searchResult':s,}

    return render(request, 'pages/searchResult.html',context)


def add(request):
    return render(request, 'pages/addPage.html')


def active(request):
    
    context={
        'student':Student.objects.all(),
    }
    
    return render(request, 'pages/activeInActive.html',context)
    


def edit(request):
    return render(request, 'pages/EditPage.html')


def assign(request):
    assign={
        'dep':Student.objects.all(),
    }
    return render(request, 'pages/assignDep.html',assign)
