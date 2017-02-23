from django.contrib import admin

from .models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'is_visible')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
