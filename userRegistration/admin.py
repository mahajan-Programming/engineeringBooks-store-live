from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from userRegistration.models import UserPersonalInfo,NewBook,Calc,WorkShopUniForm,File

# admin.site.register(UserPersonalInfo)
# admin.site.register(NewBook)
# admin.site.register(Calc)
# admin.site.register(WorkShopUniForm)
# # admin.site.register(File)


@admin.register(File)
class Vehicle(ImportExportModelAdmin):
    pass

@admin.register(WorkShopUniForm)
class Vehicle(ImportExportModelAdmin):
    pass

@admin.register(Calc)
class Vehicle(ImportExportModelAdmin):
    pass

@admin.register(NewBook)
class Vehicle(ImportExportModelAdmin):
    pass

@admin.register(UserPersonalInfo)
class Vehicle(ImportExportModelAdmin):
    pass