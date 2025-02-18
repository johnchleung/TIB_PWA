from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

def index(request):
    questions = ApiQuestion.objects.all()
    return render(request, 'index.html', {'questions': questions})

def offline(request):
    return render(request, 'offline.html')

class TibView(viewsets.ModelViewSet):
    queryset = Tib.objects.all()
    serializer_class = TibSerializer
