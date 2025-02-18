from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

def index(request):
    results = General.objects.all()
    return render(request, 'index.html', {'results': results})

def offline(request):
    return render(request, 'offline.html')

class TibView(viewsets.ModelViewSet):
    queryset = Tib.objects.all()
    serializer_class = TibSerializer
