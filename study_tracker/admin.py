from django.contrib import admin
from .models import Course,Semester,Grade

# Register your models here.


admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Grade)