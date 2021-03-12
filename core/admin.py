from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {"fields": ("email", "password"), }),
        (_('Personal Info'), {"fields": ("name", "pp",), }),
        (_('Permissions'), {
         "fields": ("is_active", "is_staff", "is_superuser"), }),
        (_("Important dates"), {"fields": ("last_login",)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Movie)
admin.site.register(models.Review)
admin.site.register(models.Person)
admin.site.register(models.Award)
admin.site.register(models.Genre)
admin.site.register(models.Cast)
admin.site.register(models.Production)
admin.site.register(models.Profession)
admin.site.register(models.Language)
admin.site.register(models.Rating)
admin.site.register(models.Photo)
