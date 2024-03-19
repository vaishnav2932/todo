from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,CreateView
from todo_app.forms import register,loginform,taskform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from todo_app.models import task
from django.utils.decorators import method_decorator

# Create your views here.










def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper  

def mylogin(fn):
    def wrapper(request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=task.objects.get(id=id)
        if obj.user!=request.user:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper    


@method_decorator(signin_required,name='dispatch')
class Registerview(View):
    def get(self,request,*args,**kwrags):
        form=register()
        return render(request,"reg.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=register(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            print(form.cleaned_data)
        form=register()
        return render(request,"reg.html",{"form":form})


class signin(View):
    def get(self, request, *args, **kwargs):
        form = loginform()
        return render(request, "login.html", {"form": form})
        

    def post(self, request,*arga,**kwargs):
        form = loginform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u_name = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            print(u_name,pwd)
            user_obj = authenticate(request, username=u_name, password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("task_add")
            else:
                print('false')
                return redirect("reg")
        else:
            print('Form is invalid.')
            print(form.errors)
            return redirect("reg")
        
class signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)  
        return redirect("signin")      

    
        
class home(View):
    def get(self,request):
        return render(request,"home.html")    
     
class taskadd(View):
    def get(self,request,*args,**kwargs):
        form=taskform()    
        data=task.objects.filter(user=request.user).order_by('complete')
        return render(request,"task_add.html",{"form":form,"data":data})
    
    def post(self,request,*args,**kwargs):
        form=taskform(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            return redirect('task_add')
        data=task.objects.filter(user=request.user)

        return render(request,"task_add.html", {"form":form,"data":data})

class taskedit(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=task.objects.get(id=id)
        if obj.complete==False:
            obj.complete=True
            obj.save()
        elif obj.complete==True:
            obj.complete=False
            obj.save()
        return redirect("task_add")   

@method_decorator(mylogin,name='dispatch')
class deletetask(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        task.objects.filter(id=id).delete()
        return redirect("task_add")
    

class user_delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        User.objects.get(id=id).delete()
        return redirect("reg")
