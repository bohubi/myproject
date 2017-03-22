from django.contrib import admin

# Register your models here.
from .models import Restaurant, MenuCategory, MenuItem

admin.site.register(Restaurant)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
