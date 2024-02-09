from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/<str:pk>/', views.tasks, name='tasks'),
]