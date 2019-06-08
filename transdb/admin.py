from django.contrib import admin

# Register your models here.
from .models import TransDB, FamilyDB

class TransDBAdmin(admin.ModelAdmin):
    pass

class FamilyDBAdmin(admin.ModelAdmin):
    pass

admin.site.register(TransDB)
admin.site.register(FamilyDB)