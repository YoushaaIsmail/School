from django.contrib import admin
from .models import Account,Parent
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(Account)
admin.site.register(Parent)
# @admin.register(Account)
# class UserAdmin(BaseUserAdmin):
#     add_fieldsets=(
#         (None,{
#         'classes':('wide',),
#         'fields':('username','email','phone','password1','password2','photo','identity','first_name','last_name'),
#         }),
#     )


    