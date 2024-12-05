from django.contrib import admin
from .models import TodoItem, BarberItem, ServiceItem, Appointment

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(BarberItem)
admin.site.register(ServiceItem)
admin.site.register(Appointment)
