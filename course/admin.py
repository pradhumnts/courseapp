from django.contrib import admin
from .models import Course, Question, Category, Child, Genre

# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Child)
admin.site.register(Genre)