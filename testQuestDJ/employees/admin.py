from django.contrib import admin
from .models import *

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "position", "acceptance_date", "email", "manager")
    list_display_links = ("id", "full_name", "email")
    search_fields = ("id", "full_name", "email")

admin.site.register(Employees, EmployeesAdmin)


class PositionsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "weight")
    list_display_links = ("id", "name", "weight")
    search_fields = ("id", "name")

admin.site.register(Positions, PositionsAdmin)
