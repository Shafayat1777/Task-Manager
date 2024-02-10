from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRouts),
    path('tasks/', views.getTasks),
    path('tasks/<str:pk>', views.getTask),
    path('add/', views.addTask),
    path('update/<str:pk>', views.updateTask),
    path('delete/<str:pk>', views.deleteTask),
]
