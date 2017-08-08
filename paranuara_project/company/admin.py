from django.contrib import admin

from .models import Employee, Company, Fruit, Vegetable


admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Fruit)
admin.site.register(Vegetable)
