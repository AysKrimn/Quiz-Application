
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from quiz.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index" ),
    path('İletişim/',main, name="main" ),
    path('Dersler/',ders, name="ders" ),
    path('Anasayfa/',anasayfa, name="anasayfa" ),
    # DERSLER
    path('Html/',html, name="html" ),
    path('Html/<int:pk>/', html_detail, name='html_detail'),

    path('Css/',css, name="css" ),
    path('Css/<int:pk>/', css_detail, name='css_detail'),

    path('Bootstrap/',bootstrap, name="bootstrap" ),
    path('Bootstrap/<int:pk>/', bootstrap_detail, name='bootstrap_detail'),

    path('Javascript/',java, name="java" ),
    path('Javascript/<int:pk>/', java_detail, name='java_detail'),

    path('Python/',python, name="python" ),
    path('Python/<int:pk>/', python_detail, name='python_detail'),

    path('Django/',django, name="django" ),
    path('Django/<int:pk>/', django_detail, name='django_detail'),

    path('C#/',cşarp, name="cşarp" ),
    path('C#/<int:pk>/', cşarp_detail, name='cşarp_detail'),

    path('C++/',cplus, name="cplus" ),
    path('C++/<int:pk>/', cplus_detail, name='cplus_detail'),

   
    

  
    #SINAV
     path('Htmlquiz/',htmlq, name="htmlq" ),
     path('Cssquiz/',cssq, name="cssq" ),
     path('Bootstrapquiz/',bootstrapq, name="bootstrapq" ),
     path('Javascriptquiz/',javaq, name="javaq" ),
     path('Pythonquiz/',pythonq, name="pythonq" ),
     path('Djangoquiz/',djangoq, name="djangoq" ),
     path('C#quiz/',cşarpq, name="cşarpq" ),
     path('C++quiz/',cplusq, name="cplusq" ),

     #FİNAL
     path('Final/', start_quiz, name='start_quiz'),
     path('FinalSınav/', quiz, name='quiz'),
     path('FinalSonuç/', result, name='result'),

     #USER
    path('Giriş/', loginUser, name="loginUser"),
    path('KayıtOl/', RegisterUser, name="RegisterUser"),
    path('logout/',logoutUser,name='logoutUser'),

    path('Profil/',profil,name='profil'),
    path('Profil/deleteStatu/<sid>/', deleteStatu, name="deleteStatu"), # Yetenek Silme
    





]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
