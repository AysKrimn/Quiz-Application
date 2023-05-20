
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from quiz.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index" ),
    path('main/',main, name="main" ),
    path('ders/',ders, name="ders" ),
    path('anasayfa/',anasayfa, name="anasayfa" ),
    # DERSLER
    path('html/',html, name="html" ),
    path('<int:pk>/', html_detail, name='html_detail'),
    path('css/',css, name="css" ),
    path('js/',js, name="js" ),
    path('bootstrap/',bootstrap, name="bootstrap" ),
    path('python/',python, name="python" ),
    path('django/',django, name="django" ),
    path('c#/',c, name="c" ),
    path('c++/',cc, name="cc" ),

     #USER
    path('login/', loginUser, name="loginUser"),
    path('register/', RegisterUser, name="RegisterUser"),
    path('logout/',logoutUser,name='logoutUser'),

    path('profil/',profil,name='profil'),
    path('profil/deleteStatu/<sid>/', deleteStatu, name="deleteStatu"), # Yetenek Silme
    





]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
