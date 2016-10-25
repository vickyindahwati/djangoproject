from django.contrib import admin
from django.contrib import admin
from library.models import Category, Book, Pengarang
from library.models import UserProfile

# Register your models here.
admin.site.register(Pengarang)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(UserProfile)
