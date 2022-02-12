from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Internship)
admin.site.register(Resource)
