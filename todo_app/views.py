from django.shortcuts import render,redirect
from django.views.generic import View
from todo_app.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


class Signup(View):
    def get(self,request):
        form = register()
        return render(request,'signup.html',{'form':form})
    
    def post(self,request):
        form = register(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
        return redirect('sign-in') 

class Signin(View):  
    def get(self,request):
        form = loginform()
        return render(request,"login.html",{"form":form})

    def post(self,request):
        form = loginform(request.POST)    
        if form.is_valid():
            u_name = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user_obj = authenticate(request,username=u_name,password=pwd)

            if user_obj:
                login(request,user_obj)
                return redirect("add-task")
            else:
                return render(request,"login.html",{"form":form,"error":"Invalid username or password"})
       

               

              
             
class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)  
        return redirect("sign-in")

class addtask(View):
    def get(self,request):
        form = task_add()
        data = task.objects.filter(user=request.user).order_by('complete')
        return render(request,"task.html",{"form":form,"data":data})
    
    def post(self,request):
        form = task_add(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect("add-task")
        data = task.objects.filter(user=request.user)
        return render(request,"task.html",{"form":form,"data":data})


class task_edit(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        obj = task.objects.get(id=id)
        if obj.complete == False:
            obj.complete = True
            obj.save()
        elif obj.complete == True:
            obj.complete = False
            obj.save()
        return redirect("add-task")
        
class task_delete(View):
    def get(self,request,*args,**kwargs):
        id =kwargs.get("pk")
        task.objects.filter(id=id).delete()
        return redirect("add-task")        
         


        

