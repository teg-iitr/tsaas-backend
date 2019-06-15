from django.contrib import admin

# Register your models here.
from .models import Family, Member, Trip, OriginDestination, Mode

class TransDBAdmin(admin.ModelAdmin):
    pass

class FamilyDBAdmin(admin.ModelAdmin):
    pass

admin.site.register(Family)
admin.site.register(Member)
admin.site.register(Trip)
admin.site.register(OriginDestination)
admin.site.register(Mode)