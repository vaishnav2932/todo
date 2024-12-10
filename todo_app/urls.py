from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path('signup/',Signup.as_view(),name='sign-up'),
   path('',Signin.as_view(),name='sign-in'),
   path('task/',addtask.as_view(),name='add-task'),
   path('task/edit/<int:pk>',task_edit.as_view(),name='edit'),
   path('task/delete/<int:pk>',task_delete.as_view(),name='delete'),
   path('logout/',signout.as_view(),name='log-out')
]