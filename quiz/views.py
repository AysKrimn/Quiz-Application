from django.shortcuts import render,redirect,HttpResponseRedirect
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
    css=Css.objects.all()
    context={
        'css':css
    }
    return render(request,'dersler/css.html',context)

def  css_detail(request,pk):
	css = Css.objects.get(pk=pk)
	context = {
	'css': css,
	}
	return  render(request, 'detay/cssdetay.html', context)

def bootstrap (request):     
    bootstrap=Bootstrap.objects.all()
    context={
        'bootstrap':bootstrap
    }
    return render(request,'dersler/bootstrap.html',context)

def  bootstrap_detail(request,pk):
	bootstrap = Bootstrap.objects.get(pk=pk)
	context = {
	'bootstrap': bootstrap,
	}
	return  render(request, 'detay/bootstrapdetay.html', context)

def java (request):     
    java=Java.objects.all()
    context={
        'java':java
    }
    return render(request,'dersler/js.html',context)

def  java_detail(request,pk):
	java = Java.objects.get(pk=pk)
	context = {
	'java': java,
	}
	return  render(request, 'detay/jsdetay.html', context)

def python (request):     
   
    python=Python.objects.all()
    context={
        'python':python
    }
    return render(request,'dersler/python.html',context)

def  python_detail(request,pk):
	python = Python.objects.get(pk=pk)
	context = {
	'python': python,
	}
	return  render(request, 'detay/pythondetay.html', context)

def django (request):     
   
    django=Django.objects.all()
    context={
        'django':django
    }
    return render(request,'dersler/django.html',context)

def  django_detail(request,pk):
	django = Django.objects.get(pk=pk)
	context = {
	'django': django,
	}
	return  render(request, 'detay/djangodetay.html', context)

def cşarp (request):     
   
    cşarp=C.objects.all()
    context={
        'cşarp':cşarp
    }
    return render(request,'dersler/c#.html',context)

def  cşarp_detail(request,pk):
	cşarp = C.objects.get(pk=pk)
	context = {
	'cşarp': cşarp,
	}
	return  render(request, 'detay/c#detay.html', context)

def cplus (request):     
   
    cplus=CPLUS.objects.all()
    context={
        'cplus':cplus
    }
    return render(request,'dersler/c++.html',context)

def  cplus_detail(request,pk):
	cplus = CPLUS.objects.get(pk=pk)
	context = {
	'cplus': cplus,
	}
	return  render(request, 'detay/c++detay.html', context)

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
    
def cssq(request):
    
    if request.method == 'POST':
        score = 0
        error_count = 0
        blank_count = 0
        wrong_cssq = []

        cssq = CssQ.objects.all()
       

        total_cssq = cssq.count()

        for question in cssq:
            selected_option = request.POST.get(str(question.id))
            if selected_option:
                if selected_option == question.correct_answer:
                    score += 10
                else:
                    error_count += 1
                    wrong_cssq.append({
                        'question': question,
                        'selected_option': selected_option
                    })
            else:
                blank_count += 1

        success_percentage = "{:.2f}".format((score / (total_cssq * 10)) * 100)
        error_percentage = "{:.2f}".format((error_count / total_cssq) * 100)
        blank_percentage = "{:.2f}".format((blank_count / total_cssq) * 100)

        return render(request, 'sınav/cssresult.html', {
            'score': score,
            'error_count': error_count,
            'blank_count': blank_count,
            'success_percentage': success_percentage,
            'error_percentage': error_percentage,
            'blank_percentage': blank_percentage,
            'wrong_cssq': wrong_cssq
        })

    else:
        cssq = CssQ.objects.all()
        return render(request, 'sınav/cssquiz.html', {'cssq': cssq})
    
def bootstrapq(request):
    
    if request.method == 'POST':
        score = 0
        error_count = 0
        blank_count = 0
        wrong_bootstrapq = []

        bootstrapq = BootstrapQ.objects.all()
       

        total_bootstrapq = bootstrapq.count()

        for question in bootstrapq:
            selected_option = request.POST.get(str(question.id))
            if selected_option:
                if selected_option == question.correct_answer:
                    score += 10
                else:
                    error_count += 1
                    wrong_bootstrapq.append({
                        'question': question,
                        'selected_option': selected_option
                    })
            else:
                blank_count += 1

        success_percentage = "{:.2f}".format((score / (total_bootstrapq * 10)) * 100)
        error_percentage = "{:.2f}".format((error_count / total_bootstrapq) * 100)
        blank_percentage = "{:.2f}".format((blank_count / total_bootstrapq) * 100)

        return render(request, 'sınav/bootstrapresult.html', {
            'score': score,
            'error_count': error_count,
            'blank_count': blank_count,
            'success_percentage': success_percentage,
            'error_percentage': error_percentage,
            'blank_percentage': blank_percentage,
            'wrong_bootstrapq': wrong_bootstrapq
        })

    else:
        bootstrapq = BootstrapQ.objects.all()
        return render(request, 'sınav/bootstrapquiz.html', {'bootstrapq': bootstrapq})
    
def javaq(request):
    
    if request.method == 'POST':
        score = 0
        error_count = 0
        blank_count = 0
        wrong_javaq = []

        javaq = JavaQ.objects.all()
       

        total_javaq = javaq.count()

        for question in javaq:
            selected_option = request.POST.get(str(question.id))
            if selected_option:
                if selected_option == question.correct_answer:
                    score += 10
                else:
                    error_count += 1
                    wrong_javaq.append({
                        'question': question,
                        'selected_option': selected_option
                    })
            else:
                blank_count += 1

        success_percentage = "{:.2f}".format((score / (total_javaq * 10)) * 100)
        error_percentage = "{:.2f}".format((error_count / total_javaq) * 100)
        blank_percentage = "{:.2f}".format((blank_count / total_javaq) * 100)

        return render(request, 'sınav/jsresult.html', {
            'score': score,
            'error_count': error_count,
            'blank_count': blank_count,
            'success_percentage': success_percentage,
            'error_percentage': error_percentage,
            'blank_percentage': blank_percentage,
            'wrong_javaq': wrong_javaq
        })

    else:
        javaq = JavaQ.objects.all()
        return render(request, 'sınav/jsquiz.html', {'javaq': javaq})
    
def pythonq(request):

    if request.method == 'POST':
        score = 0
        error_count = 0
        blank_count = 0
        wrong_pythonq = []

        pythonq = PythonQ.objects.all()
       

        total_pythonq = pythonq.count()

        for question in pythonq:
            selected_option = request.POST.get(str(question.id))
            if selected_option:
                if selected_option == question.correct_answer:
                    score += 10
                else:
                    error_count += 1
                    wrong_pythonq.append({
                        'question': question,
                        'selected_option': selected_option
                    })
            else:
                blank_count += 1

        success_percentage = "{:.2f}".format((score / ( total_pythonq * 10)) * 100)
        error_percentage = "{:.2f}".format((error_count /  total_pythonq) * 100)
        blank_percentage = "{:.2f}".format((blank_count /  total_pythonq) * 100)

        return render(request, 'sınav/pythonresult.html', {
            'score': score,
            'error_count': error_count,
            'blank_count': blank_count,
            'success_percentage': success_percentage,
            'error_percentage': error_percentage,
            'blank_percentage': blank_percentage,
            'wrong_pythonq': wrong_pythonq
        })

    else:
        pythonq = PythonQ.objects.all()
        return render(request, 'sınav/pythonquiz.html', {'pythonq': pythonq})
    
def djangoq(request):
    
    if request.method == 'POST':
        score = 0
        error_count = 0
        blank_count = 0
        wrong_djangoq = []

        djangoq = DjangoQ.objects.all()
       

        total_djangoq = djangoq.count()

        for question in djangoq:
            selected_option = request.POST.get(str(question.id))
            if selected_option:
                if selected_option == question.correct_answer:
                    score += 10
                else:
                    error_count += 1
                    wrong_djangoq.append({
                        'question': question,
                        'selected_option': selected_option
                    })
            else:
                blank_count += 1

        success_percentage = "{:.2f}".format((score / (  total_djangoq * 10)) * 100)
        error_percentage = "{:.2f}".format((error_count /   total_djangoq) * 100)
        blank_percentage = "{:.2f}".format((blank_count /   total_djangoq) * 100)

        return render(request, 'sınav/djangoresult.html', {
            'score': score,
            'error_count': error_count,
            'blank_count': blank_count,
            'success_percentage': success_percentage,
            'error_percentage': error_percentage,
            'blank_percentage': blank_percentage,
            'wrong_djangoq': wrong_djangoq
        })

    else:
        djangoq = DjangoQ.objects.all()
        return render(request, 'sınav/djangoquiz.html', {'djangoq': djangoq})
    
def cşarpq(request):
    
    if request.method == 'POST':
        score = 0
        error_count = 0
        blank_count = 0
        wrong_cşarpq = []

        cşarpq = CQ.objects.all()
       

        total_cşarpq = cşarpq.count()

        for question in cşarpq:
            selected_option = request.POST.get(str(question.id))
            if selected_option:
                if selected_option == question.correct_answer:
                    score += 10
                else:
                    error_count += 1
                    wrong_cşarpq.append({
                        'question': question,
                        'selected_option': selected_option
                    })
            else:
                blank_count += 1

        success_percentage = "{:.2f}".format((score / (  total_cşarpq * 10)) * 100)
        error_percentage = "{:.2f}".format((error_count /   total_cşarpq) * 100)
        blank_percentage = "{:.2f}".format((blank_count /   total_cşarpq) * 100)

        return render(request, 'sınav/c#result.html', {
            'score': score,
            'error_count': error_count,
            'blank_count': blank_count,
            'success_percentage': success_percentage,
            'error_percentage': error_percentage,
            'blank_percentage': blank_percentage,
            'wrong_cşarpq': wrong_cşarpq
        })

    else:
        cşarpq = CQ.objects.all()
        return render(request, 'sınav/c#quiz.html', {'cşarp': cşarpq})
    
def cplusq(request):
    
    if request.method == 'POST':
        score = 0
        error_count = 0
        blank_count = 0
        wrong_cplusq = []

        cplusq = CPLUSQ.objects.all()
       

        total_cplusq = cplusq.count()

        for question in cplusq:
            selected_option = request.POST.get(str(question.id))
            if selected_option:
                if selected_option == question.correct_answer:
                    score += 10
                else:
                    error_count += 1
                    wrong_cplusq.append({
                        'question': question,
                        'selected_option': selected_option
                    })
                    
            else:
                blank_count += 1

        success_percentage = "{:.2f}".format((score / (  total_cplusq * 10)) * 100)
        error_percentage = "{:.2f}".format((error_count /   total_cplusq) * 100)
        blank_percentage = "{:.2f}".format((blank_count /   total_cplusq) * 100)

        return render(request, 'sınav/c++result.html', {
            'score': score,
            'error_count': error_count,
            'blank_count': blank_count,
            'success_percentage': success_percentage,
            'error_percentage': error_percentage,
            'blank_percentage': blank_percentage,
            'wrong_cplusq': wrong_cplusq
        })

    else:
        cplusq = CPLUSQ.objects.all()
        return render(request, 'sınav/c++quiz.html', {'cplusq': cplusq})
#QUİZ BİTİŞ

#FİNAL SINAV
def start_quiz(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect('quiz')

    return render(request, 'Final/Finalstart.html')

def quiz(request):
    if request.method == 'POST':
        username = request.session.get('username')
        questions = Question.objects.all()
        quiz_result = QuizResult.objects.create(username=username)
        score = 0
        correct_questions = []
        incorrect_questions = []

        for question in questions:
            selected_option = request.POST.get(f"option_{question.id}")
            if selected_option == question.correct_option:
                score += 10
                correct_questions.append(question)
            else:
                incorrect_questions.append(question)
        
        quiz_result.score = score
        quiz_result.correct_questions = len(correct_questions)
        quiz_result.incorrect_questions.set(incorrect_questions)
        quiz_result.success_percentage = (score / (len(questions) * 10)) * 100
        quiz_result.save()

        request.session['quiz_result_id'] = quiz_result.id
        return redirect('result')

    return render(request, 'Final/Finalquiz.html', {'questions': Question.objects.all()})

def result(request):
    quiz_result_id = request.session.get('quiz_result_id')
    if quiz_result_id:
        quiz_result = QuizResult.objects.get(id=quiz_result_id)
        incorrect_questions = quiz_result.incorrect_questions.all()

        context = {
            'quiz_result': quiz_result,
            'incorrect_questions': incorrect_questions,
        }
        return render(request, 'Final/Finalresult.html', context)

    return redirect('start_quiz')

#FİNAL SINAV BİTİŞ

def profil (request):     
   
    context={}
    # user = User.objects.get(username = request.user)
    # userinfo = UserInfo.objects.get(user=user)
    userinfo = None
    user = request.user
    userinfo = UserInfo.objects.filter(user=user).first()
    
    if userinfo is None:
        userinfo = UserInfo.objects.create(user=user)
    
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
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        text = request.POST["text"]
        
        contact = Contact(name=name,email=email,text=text,)
        contact.save()
        return HttpResponseRedirect("/İletişim/")
    
    return render(request,'main.html')

def anasayfa (request):
    context = {
        
    }
    return render(request,'anasayfa.html',context)