from django.contrib import admin

# Register your models here.
from userRegistration.models import UserPersonalInfo,NewBook,Calc,WorkShopUniForm,File

admin.site.register(UserPersonalInfo)
admin.site.register(NewBook)
admin.site.register(Calc)
admin.site.register(WorkShopUniForm)
admin.site.register(File)