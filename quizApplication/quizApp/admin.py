from django.contrib import admin
from .models import *

class QuizesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','detail' ,'date_joined', 'timer')
    list_filter = ('title', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail')
    list_filter = ('title', 'detail')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Quizes, QuizesAdmin)