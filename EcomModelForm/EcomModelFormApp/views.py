
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from . forms import *
from . models import *

# Create your views here.
@login_required
def home(request):
    form=EcomForm()
    return render(request, 'home.html', {'form':form})

def enter(request):
    try:
        if request.method == "POST":
            form = EcomForm(request.POST)
            if form.is_valid():  
                form.save() 
                return render(request, 'home.html', {'form': form, "msg": "Details Added"})
            else:
                
                return render(request, 'home.html', {'form': form, "msg": "Invalid data provided."})
        else:
            form = EcomForm() 
            return render(request, 'home.html', {'form': form})
    except Exception as e:
        print(e)  
        return HttpResponse("Error occurred")

   
def view_list(request):
    detail=Ecom.objects.all()
    return render(request, 'view_list.html', {'detail': detail})

def delete(request,id):
    item=Ecom.objects.filter(id=id)
    if item.exists():
        item.delete()
    else:
        return HttpResponse("Item not found")
    return render(request, 'view_list.html')

def edit(request,id):
    item=get_object_or_404(Ecom,id=id)
    form = EcomForm(instance=item)
    if request.method == "POST":
        form = EcomForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('view_list')
    return render(request, 'edit.html', {'form': form})



def loginview(request):
    if request.method == "POST":
        # Use `.get()` to avoid MultiValueDictKeyError
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username and password are provided
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a home page or another page after login
            else:
                return HttpResponse("Invalid credentials")
        else:
            return HttpResponse("Please enter both username and password")
    
    # If GET request, render the login page
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    try:
        form = UserCreationForm(request.POST)
        if request.method == "POST":
            if form.is_valid():   
                form.save() 
                return redirect('login')  
            return render(request, 'sign_up.html', {'form': userform,'msg':'Invalid login'})
                         
        else:
            form=UserCreationForm()
            return render(request, 'sign_up.html', {'form': userform,'msg':'Invalid submission'})
    except Exception as e:
            print(e)
            userform = UserCreationForm()
            return render(request, 'sign_up.html', {'form': userform})
    
def Resethome(request):
    return render(request,'ResetPassword.html')

def resetPassword(request):
    uname = request.POST['uname']
    newpwd=request.POST['password']

    try:
            user=User.objects.get(username=uname)
            if user is not None:
                user.set_password(newpwd)
                user.save()
                return render(request,"ResetPassword.html",{"msg":"Password Reset Successfully"})
    except Exception as e:
            print(e)
            return render(request,"ResetPassword.html",{"msg":"Password Reset Failed"})




    
