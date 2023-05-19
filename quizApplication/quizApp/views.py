from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index (request):     
   
    context={}
    return render(request,'index.html',context)

def profil (request):     
   
    context={}
    return render(request,'profile.html',context)

#USER Alanı
def loginUser(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        
        harfet = False
        for harf in username:
            if harf == "@":
                harfet = True
        # find bulursa index numarasını verir, bulamazsa -1 değeri döndürür
        # if username.find("@") != -1:
        #     harfet = True
                
        if username[-4:] == ".com" and harfet: # berkay@gmail.com = berkay
           
                
            try:
                user = User.objects.get(email=username)
                username = user.username
            except:
                messages.warning(request, "Email kayıtlı değil!")
                return redirect("loginUser")
            
        
        user = authenticate(username = username, password= password)
        
        if user is not None:
            login(request,user)
            return redirect("main")
        else:
            messages.warning(request, "Kullanıcı adı veya şifre yanlış!")
            return redirect("login")
    
    return render(request,'login.html')

def RegisterUser (request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1") 
        password2 = request.POST.get("password2")
        
        harfup = False
        harfnum = False
        if password1 == password2:
            for harf in password1:
                if harf.isupper():
                    harfup = True
                if harf.isnumeric():
                    harfnum = True
            
            if harfup and harfnum and len(password1)>=6:
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        
                        user = User.objects.create_user(username=username, password=password1, email=email,
                                                        first_name=name, last_name=surname)
                        user.save()
                        return redirect("loginUser")
                    else:
                        messages.warning(request, "Bu email zaten kullanılıyor!")
                        return redirect("RegisterUser")
                else:
                    messages.warning(request, "Bu kullanıcı adı başkası tarafından kullanılıyor!")
                    return redirect("RegisterUser")
            else:
                messages.warning(request, "Şifre en az 6 karakter olmalı!")
                messages.warning(request, "Şifrede bir büyük harf olmalı!")
                messages.warning(request, "Şifrede bir sayı olmalı!")
                return redirect("RegisterUser")
        else:
            messages.warning(request, "Şifreler aynı değil!")
            return redirect("RegisterUser")
    return render(request,'kayıtol.html')

def logoutUser(request):
    logout(request)
    return redirect('loginUser')


def main (request):
    context = {
        
    }
    return render(request,'main.html',context)