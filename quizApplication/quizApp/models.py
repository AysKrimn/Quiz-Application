from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(("Kategori"), max_length=50)
    
    def __str__(self):
        return self.title
class Post(models.Model):
    category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    title = models.CharField(("Quiz Adı"), max_length=50)
    Qtext = models.TextField(("Quiz Açıklması"), max_length=500, blank=True, null=True)
    Btext = models.TextField(("Quiz Banner"), max_length=500, blank=True, null=True)
    date_now = models.DateField(("Tarih"), auto_now_add=True, null=True)
    süre = models.DurationField(("Sınav Süresi"),blank=True, null=True)

    def __str__(self):
        return self.title

# USER MODEL
class UserInfoStatus(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    title=models.CharField(("Yetenek Adı"), max_length=50)
    statu=models.IntegerField(("Yetenek Değeri"), default=0)

    def __str__(self):
        return "KULLANICI: "+ self.user.username +"...........YETENEK: "+ self.title
    
class UserInfo(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    password=models.CharField(("Şifre"), max_length=50)
    job= models.CharField(("İş"), max_length=50,default="-")
    image=models.FileField(("Fotoğraf"), upload_to=None, max_length=100,default='None/download.jpg')
    phone=models.CharField(("Telefon Numarası"), max_length=50, default="-")
    adress=models.CharField(("Adres"), max_length=50, default="-")
    status=models.ManyToManyField(UserInfoStatus, verbose_name=("Yetenekler") )

    def __str__(self):
        return self.user.username


