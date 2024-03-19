from django.shortcuts import render  
from rest_framework.viewsets import ViewSet
from todo_app.models import task
from api.serializer import taskserializer
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class taskviewset(ViewSet):
    # authentication_classes=[authentication.BasicAuthentication]
    # permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=task.objects.all()
        serializers=taskserializer(qs,many=True)
        return Response(data=serializers.data)
    
    def create(self,request,*args,**kwargs):
        serializer=taskserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=task.objects.get(id=id)
        serialisers=taskserializer(qs)
        return Response(data=serialisers.data)
    
