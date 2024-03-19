from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import taskviewset
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()

router.register("v2/task",taskviewset,basename="taskview")

urlpatterns =[
    path("token",ObtainAuthToken.as_view())
     



]+router.urls

