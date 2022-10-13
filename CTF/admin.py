from django.contrib import admin

from CTF.models import User


# from django.contrib import
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, AuthorAdmin)