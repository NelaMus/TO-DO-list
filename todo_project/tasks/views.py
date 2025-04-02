from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def home(request):
    return render(request, 'tasks/index.html')  # Odkaz na HTML šablonu

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])  # Definuje API endpoint, který odpovídá na GET requesty
def task_list(request):
    return Response({"message": "Seznam úkolů zatím není dostupný."})  # Vrátí JSON odpověď
