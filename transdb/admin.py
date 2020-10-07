from django.contrib import admin

# Register your models here.
from .models import (
    Family,
    Member,
    Trip,
    OriginDestination,
    MemberDistrict,
    Mode,
    CollegeList,
    Feedback,
    SurveyList,
    ResponseTime,
    SurveyType,
    PtSurvey,
    PtSurveyRating,
    AQIPerceptionSurvey
    )


admin.site.site_header = 'TSaaS Admin Dashboard'

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('memberID', 'familyID', 'created_at')
    list_filter = ('gender','monthlyIncome','householdHead')


@admin.register(Family)
class FamilyDBAdmin(admin.ModelAdmin):
    list_display = ('familyID', 'collegeID', 'noOfMembers')
    list_filter = ('collegeID', 'noOfMembers', 'familyIncome', 'homeState', 'nameOfDistrict')


@admin.register(SurveyList)
class SurveyListAdmin(admin.ModelAdmin):
    list_display = ('surveyID', 'surveyType')
    list_filter = ('surveyType',)


@admin.register(SurveyType)
class SurveyTypeAdmin(admin.ModelAdmin):
    list_display = ('surveyTypeID', 'surveyFormat')
    list_filter = ('surveyFormat',)


@admin.register(ResponseTime)
class ResponseTimeAdmin(admin.ModelAdmin):
    list_display = ('responseTimeID', 'surveyID', 'surveyStartTime', 'surveyEndTime')


@admin.register(MemberDistrict)
class MemberDistrictAdmin(admin.ModelAdmin):
    list_display = ('memberDistrictId','memberID','memberDistrict')
    list_filter = ('memberDistrict',)


@admin.register(CollegeList)
class CollegeListAdmin(admin.ModelAdmin):
    list_display = ('collegeID', 'collegeName', 'surveyTypeID')
    list_filter = ('surveyTypeID',)


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('tripID', 'memberID')


@admin.register(OriginDestination)
class ODAdmin(admin.ModelAdmin):
    list_display = ('originDestinationID', 'tripID', 'travelDistance', 'fare')


@admin.register(Mode)
class ModeAdmin(admin.ModelAdmin):
    list_display = ('modeID', 'tripID', 'modeName')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','feedback_time',)


@admin.register(PtSurvey)
class PtSurveyAdmin(admin.ModelAdmin):
    list_display = ('personID', 'collegeID', 'surveyID')
    list_filter = ('gender', 'monthlyIncome')


@admin.register(PtSurveyRating)
class PtSurveyRatingAdmin(admin.ModelAdmin):
    list_display = ('ptSurveyRatingId', 'personID',)


@admin.register(AQIPerceptionSurvey)
class AQIPerceptionSurveyAdmin(admin.ModelAdmin):
    list_display = ('memberID', 'gender', 'age')
    

