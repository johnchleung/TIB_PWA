from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import *

def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})

def offline(request):
    return render(request, 'offline.html')

