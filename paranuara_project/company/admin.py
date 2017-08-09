from django.contrib import admin

from .models import Employee, Company, Food


admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Food)
