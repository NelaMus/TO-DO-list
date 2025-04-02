from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .views import task_list, home  # Importujeme novou funkci


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', home, name='home'),  # Nastaví hlavní stránku
    path('api/tasks/', task_list, name='task-list'),  # API endpoint

]

