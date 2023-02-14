from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_page(request):
    message=''
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            message = 'Identifiants valides.'
            return redirect("/water/dashbord/")
        else:
            message = 'Identifiants invalides.'
    
    return render(request,'authenticate/login.html',context={'message':message})

def logout_page(request):
    logout(request)
    return redirect("/water/login/")

def registration_page(request):
    
    return render(request,'authenticate/registration.html')