from django.contrib import admin
from .models import *


class QuizesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','detail' ,'date_joined', 'timer')
    list_filter = ('title', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail')
    list_filter = ('title', 'detail')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('username', 'email')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Quizes, QuizesAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
