from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


# Create your views here.
def index (request):     
   
    context={}
    return render(request,'index.html',context)

def ders (request):     
   
    context = {}
   
    return render(request,'dersler.html',context)

# DERSLER

def  html(request):
    
	html = Html.objects.all()
   
	context = {
	'html': html,
    
	}
    
	return  render(request, 'dersler/html.html', context)

def  html_detail(request,pk):
	html = Html.objects.get(pk=pk)
	context = {
	'html': html,
	}
	return  render(request, 'detay/htmldetay.html', context)

def css (request):     
   
    context={}
    return render(request,'dersler/css.html',context)

def js (request):     
   
    context={}
    return render(request,'dersler/js.html',context)

def bootstrap (request):     
   
    context={}
    return render(request,'dersler/bootstrap.html',context)

def python (request):     
   
    context={}
    return render(request,'dersler/python.html',context)

def django (request):     
   
    context={}
    return render(request,'dersler/django.html',context)

def c (request):     
   
    context={}
    return render(request,'dersler/c#.html',context)

def cc (request):     
   
    context={}
    return render(request,'dersler/c++.html',context)
# QUİZLER
def htmlq(request):
    
    if request.method == 'POST':
        score = 0
        error_count = 0
        blank_count = 0
        wrong_htmlq = []

        htmlq = HtmlQ.objects.all()
       

        total_htmlq = htmlq.count()

        for question in htmlq:
            selected_option = request.POST.get(str(question.id))
            if selected_option:
                if selected_option == question.correct_answer:
                    score += 10
                else:
                    error_count += 1
                    wrong_htmlq.append({
                        'question': question,
                        'selected_option': selected_option
                    })
            else:
                blank_count += 1

        success_percentage = "{:.2f}".format((score / (total_htmlq * 10)) * 100)
        error_percentage = "{:.2f}".format((error_count / total_htmlq) * 100)
        blank_percentage = "{:.2f}".format((blank_count / total_htmlq) * 100)

        return render(request, 'sınav/htmlresult.html', {
            'score': score,
            'error_count': error_count,
            'blank_count': blank_count,
            'success_percentage': success_percentage,
            'error_percentage': error_percentage,
            'blank_percentage': blank_percentage,
            'wrong_htmlq': wrong_htmlq
        })

    else:
        htmlq = HtmlQ.objects.all()
        return render(request, 'sınav/htmlquiz.html', {'htmlq': htmlq})
#QUİZ BİTİŞ

def profil (request):     
   
    context={}
    user = User.objects.get(username = request.user)
    userinfo = UserInfo.objects.get(user=user)
    
    if request.method=="POST": # methodun post olduğunu doğrula
        # ___PROFİL___
        if request.POST["formbutton"] == "profilChange":  # formdan gelen butonu kontrol et
            password = request.POST["password"]
            if user.check_password(password):  # parolayı kontrol et
                username = request.POST["username"]  # kullanıcı çek
                job = request.POST["job"]  # iş çek
                
                image = request.FILES.get("image")
                
                user.username = username
                user.save()
                userinfo.job = job
                userinfo.image = image
                userinfo.save()
            
                # user.save()  # kullanıcıyı kaydet
                # sayfayı resetle, aynı sayfayı tekrar yönlendir
                return redirect('profil')
            
            
            
            
           
        
        # ___NAME___
        if request.POST["formbutton"] == "nameChange":  # formdan gelen butonu kontrol et
            name = request.POST["name"]  # emaili çek
            surname = request.POST["surname"]  # emaili çek
            
            user.first_name = name  # emaili değiştir
            user.last_name = surname  # emaili değiştir
            user.save()  # kullanıcıyı kaydet
            # sayfayı resetle, aynı sayfayı tekrar yönlendir
            return redirect('profil')
            
        # ___EMAİL___
        if request.POST["formbutton"] == "emailChange": # formdan gelen butonu kontrol et
            password = request.POST["password"] # parolayı değişkene çek
            if user.check_password(password): # parolayı kontrol et
                email = request.POST["email"] # emaili çek
                user.email = email # emaili değiştir
                user.save() # kullanıcıyı kaydet
                return redirect('profil') # sayfayı resetle, aynı sayfayı tekrar yönlendir
        # ___PHONE___
        if request.POST["formbutton"] == "telChange":  # formdan gelen butonu kontrol et
            password = request.POST["password"]  # parolayı değişkene çek
            if user.check_password(password):  # parolayı kontrol et
                tel = request.POST["tel"]  # tel çek
                userinfo.phone = tel  # tel değiştir
                userinfo.save()  # kullanıcıyı kaydet
                # sayfayı resetle, aynı sayfayı tekrar yönlendir
                return redirect('profil')
        
        # ___ADDRESS___
        if request.POST["formbutton"] == "addressChange":  # formdan gelen butonu kontrol et
            address = request.POST["address"]  # tel çek
            userinfo.adress = address  # tel değiştir
            userinfo.save()  # kullanıcıyı kaydet
            # sayfayı resetle, aynı sayfayı tekrar yönlendir
            return redirect('profil')
            
                
        # ___STATU___
        if request.POST["formbutton"] == "formStatu":
            title = request.POST["title"]
            statu = request.POST["statu"]
            userstatu = UserInfoStatus(title=title,statu=statu,user=request.user)
            userstatu.save()
            
            userinfo.status.add(userstatu)
            userinfo.save()
            return redirect("profil")
            
    context.update({
        "user":user,
        "userinfo":userinfo,
    })
    return render(request,'profile.html',context)

def deleteStatu(request,sid):
    statu = UserInfoStatus.objects.get(id=sid)
    statu.delete()
    return redirect("profil")


    

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
            return redirect("anasayfa")
        else:
            messages.warning(request, "Kullanıcı adı veya şifre yanlış!")
            return redirect("loginUser")
    
    return render(request,'Giriş.html')

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

                        userinfo = UserInfo(user=user, password=password1)
                        userinfo.save()
                    
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

def anasayfa (request):
    context = {
        
    }
    return render(request,'anasayfa.html',context)