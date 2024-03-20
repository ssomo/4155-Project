from django.contrib import admin

# Register your models here.
from .models import Financial_Information, Notification

admin.site.register(Financial_Information)
admin.site.register(Notification)