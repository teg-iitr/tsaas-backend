from django.contrib import admin

# Register your models here.
from .models import (
    Family,
    Member,
    Trip,
    OriginDestination,
    Mode,
    CollegeList,
    Feedback,
    SurveyList,
    ResponseTime,
    SurveyType,
    PtSurvey,
    PtSurveyRating
    )

class TransDBAdmin(admin.ModelAdmin):
    pass

class FamilyDBAdmin(admin.ModelAdmin):
    pass

admin.site.register(SurveyList)
admin.site.register(SurveyType)
admin.site.register(ResponseTime)
admin.site.register(CollegeList)
admin.site.register(Family)
admin.site.register(Member)
admin.site.register(Trip)
admin.site.register(OriginDestination)
admin.site.register(Mode)
admin.site.register(Feedback)
admin.site.register(PtSurvey)
admin.site.register(PtSurveyRating)