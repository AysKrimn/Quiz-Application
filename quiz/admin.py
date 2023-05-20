from django.contrib import admin
from .models import *
from  embed_video.admin  import  AdminVideoMixin
# Register your models here.

# Abstract User
# AbstractUser ile kendi user modelimizin oluşturulması
# User modeline Avatar eklenecek
# Quiz Modeli
# Quiz Başlığı
# Quiz Süresi
# Quiz Banner 
# Quiz Oluşturulma Tarihi
# Quiz Kategorileri modeli
# Quiz Başlığı
# Quiz Süresi
# Quiz Banner 
# Quiz Oluşturulma Tarihi
# Quiz Kategorisi (Foregin Key)


admin.site.register(Category)
admin.site.register(Post)


# USER
admin.site.register(UserInfo)
admin.site.register(UserInfoStatus)


class  tutorialAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(tutorial, tutorialAdmin)