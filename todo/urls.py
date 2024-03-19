"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from todo_app.views import home,Registerview,signin,taskadd,taskedit,deletetask,signout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home.as_view(),name='home'),
    path('register/',Registerview.as_view(),name="reg"),
    path("signin/",signin.as_view(),name="signin"),
    path("task/",taskadd.as_view(),name="task_add"),
    path('task/edit/<int:pk>',taskedit.as_view(),name="edit"),
    path('task/delete/<int:pk>',deletetask.as_view(),name='delete'),
    path('signout/',signout.as_view(),name='signout'),
    path('api/',include("api.urls")),

]
