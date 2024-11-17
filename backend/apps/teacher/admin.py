"""from django.contrib import admin
from .models import Teacher

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'email', 'document', 'validate', 'is_active')
    list_filter = ('validate', 'is_active')
    search_fields = ('fullName', 'email', 'document')
    actions = ['validate_teacher']

    # Definir una acción para validar a un profesor
    def validate_teacher(self, request, queryset):
        queryset.update(validate=True)
        self.message_user(request, "Los profesores seleccionados han sido validados.")

    validate_teacher.short_description = "Validar profesores seleccionados"

# Registrar el modelo Teacher con la clase personalizada TeacherAdmin
admin.site.register(Teacher, TeacherAdmin)"""

