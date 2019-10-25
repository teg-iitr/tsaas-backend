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


admin.site.site_header = 'TSaaS Admin Dashboard'


class MemberAdmin(admin.ModelAdmin):
    list_display = ('memberID', 'familyID', 'created_at')
    list_filter = ('gender','monthlyIncome','householdHead')


class FamilyDBAdmin(admin.ModelAdmin):
    list_display = ('familyID', 'collegeID', 'noOfMembers')
    list_filter = ('collegeID', 'noOfMembers', 'familyIncome', 'homeState', 'nameOfDistrict')


class SurveyListAdmin(admin.ModelAdmin):
    list_display = ('surveyID', 'surveyType')
    list_filter = ('surveyType',)


class SurveyTypeAdmin(admin.ModelAdmin):
    list_display = ('surveyTypeID', 'surveyFormat')
    list_filter = ('surveyFormat',)


class ResponseTimeAdmin(admin.ModelAdmin):
    list_display = ('responseTimeID', 'surveyID', 'surveyStartTime', 'surveyEndTime')


class CollegeListAdmin(admin.ModelAdmin):
    list_display = ('collegeID', 'collegeName', 'surveyTypeID')
    list_filter = ('surveyTypeID',)


class TripAdmin(admin.ModelAdmin):
    list_display = ('tripID', 'memberID')


class ODAdmin(admin.ModelAdmin):
    list_display = ('originDestinationID', 'tripID', 'travelDistance', 'fare')


class ModeAdmin(admin.ModelAdmin):
    list_display = ('modeID', 'tripID', 'modeName')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','feedback_time',)


class PtSurveyAdmin(admin.ModelAdmin):
    list_display = ('personID', 'collegeID', 'surveyID')
    list_filter = ('gender', 'monthlyIncome')


class PtSurveyRatingAdmin(admin.ModelAdmin):
    list_display = ('ptSurveyRatingId', 'personID',)


admin.site.register(SurveyList, SurveyListAdmin)
admin.site.register(SurveyType, SurveyTypeAdmin)
admin.site.register(ResponseTime, ResponseTimeAdmin)
admin.site.register(CollegeList, CollegeListAdmin)
admin.site.register(Family, FamilyDBAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Trip, TripAdmin)
admin.site.register(OriginDestination, ODAdmin)
admin.site.register(Mode, ModeAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(PtSurvey, PtSurveyAdmin)
admin.site.register(PtSurveyRating, PtSurveyRatingAdmin)