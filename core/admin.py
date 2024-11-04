from django.contrib import admin
from .models import Teacher,aula

class aula_admin(admin.ModelAdmin):
    readonly_fields=("created",)

class teacher_admin(admin.ModelAdmin):
    readonly_fields=("created", )
# Register your models here.
admin.site.register(aula)
admin.site.register(Teacher)

