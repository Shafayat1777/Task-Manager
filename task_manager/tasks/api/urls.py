from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRouts),
    path('tasks/', views.getTasks),
    path('tasks/<str:pk>', views.getTask),
]
