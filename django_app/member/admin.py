from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import MyUser


# Register your models here.

class MyUserAdmin(UserAdmin):
    list_display = ['username', 'nickname']
    list_filter = ['is_staff', 'is_superuser', ]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('gender', 'nickname', 'email')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email'),
        }),
    )


admin.site.register(MyUser, MyUserAdmin)
