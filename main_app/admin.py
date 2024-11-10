from django.contrib import admin
from .models import Vehicle, MaintenanceWork
# Register your models here.

admin.site.register(Vehicle)
admin.site.register(MaintenanceWork)