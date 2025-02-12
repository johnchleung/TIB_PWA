from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def offline(request):
    return render(request, 'offline.html')