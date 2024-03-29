from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, TaskComplete, Login, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),
    path('complete-task/<int:pk>', TaskComplete.as_view(), name='complete-task'),
]
