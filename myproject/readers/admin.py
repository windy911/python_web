from django.contrib import admin

# Register your models here.

from .models import Series,Book
admin.site.register(Series)
admin.site.register(Book)