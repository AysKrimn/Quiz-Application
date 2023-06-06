from django.contrib import admin
from .models import *
from  embed_video.admin  import  AdminVideoMixin



admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Contact)

# USER
admin.site.register(UserInfo)
admin.site.register(UserInfoStatus)


class  tutorialAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Html, tutorialAdmin)
admin.site.register(Css, tutorialAdmin)
admin.site.register(Bootstrap, tutorialAdmin)
admin.site.register(Java, tutorialAdmin)
admin.site.register(Python, tutorialAdmin)
admin.site.register(Django, tutorialAdmin)
admin.site.register(C, tutorialAdmin)
admin.site.register(CPLUS, tutorialAdmin)

admin.site.register(HtmlQ)
admin.site.register(CssQ)
admin.site.register(BootstrapQ)
admin.site.register(JavaQ)
admin.site.register(PythonQ)
admin.site.register(DjangoQ)
admin.site.register(CQ)
admin.site.register(CPLUSQ)

admin.site.register(Question)
admin.site.register(QuizResult)
