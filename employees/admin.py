from django.contrib import admin
from .models import *
from accounts.models import User
# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Company)
admin.site.register(User)