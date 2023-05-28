from django.db import models
from django.db import models
from django.contrib.auth.models import User
from  embed_video.fields  import  EmbedVideoField

# Create your models here.




class  Html(models.Model):
   
	tutorial_Title = models.CharField(max_length=20000)
	tutorial_Body = models.TextField()
	tutorial_Video = EmbedVideoField()
    
   
    

	class  Meta:
		verbose_name_plural = "Html"

	def  __all__(self):
		return  str(self.tutorial_Title) if  self.tutorial_Title  else  " "

class HtmlQ(models.Model):
    
    question_text = models.CharField(max_length=200,null=True)
    option_a = models.CharField(max_length=100,null=True)
    option_b = models.CharField(max_length=100,null=True)
    option_c = models.CharField(max_length=100,null=True)
    option_d = models.CharField(max_length=100,null=True)
    correct_answer = models.CharField(max_length=1, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')],null=True)

    def __str__(self):
        return self.question_text       



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


