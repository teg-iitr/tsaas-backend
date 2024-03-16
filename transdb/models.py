from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models.signals import post_save
from django.db.models import Subquery, OuterRef

from django.contrib.postgres.fields import ArrayField
# Create your models here.


def create_surveyStartTimeAndSurveyEndTime(sender, **kwargs):
    if kwargs.get('created', False):
        ResponseTime.objects.get_or_create(
            surveyID=kwargs.get('instance'),
            responseTimeID=kwargs.get('instance').surveyID
        )


class IndoreStopsList(models.Model):
    stopsName = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "IndoreStopsList"


class SurveyType(models.Model):
    surveyTypeID = models.AutoField(primary_key=True)
    surveyFormat = models.CharField(max_length=100, null=True, blank=True)
    surveyURL = models.SlugField(unique=True)

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "SurveyType"


class SurveyList(models.Model):
    surveyID = models.AutoField(primary_key=True)
    surveyType = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "SurveyList"


post_save.connect(create_surveyStartTimeAndSurveyEndTime, sender=SurveyList)


class ResponseTime(models.Model):
    responseTimeID = models.IntegerField(primary_key=True)
    surveyStartTime = models.CharField(max_length=100, null=True, blank=True)
    surveyEndTime = models.CharField(max_length=100, null=True, blank=True)
    surveyID = models.ForeignKey(SurveyList, blank=True, null=True,
                                 on_delete=models.CASCADE, related_name='surveyResponseTime')

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "ResponseTimes"


class CollegeList(models.Model):
    collegeID = models.AutoField(primary_key=True)
    collegeName = models.CharField(max_length=100, default="")
    collegeURL = models.SlugField(unique=True)
    constrainField = models.CharField(max_length=100, null=True, blank=True)
    surveyTypeID = models.ForeignKey(
        SurveyType, blank=True, null=True, on_delete=models.CASCADE, related_name='surveyType')

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "CollegeList"

    def __str__(self):
        return str(self.collegeName)
    # def get_absolute_url(self):
    # 	return reverse(kwargs={'slug': self.collegeURL})


def updateCurrentCount(sender, **kwargs):
    famObj = kwargs.get('instance').familyID
    temp = famObj.currentCount + 1
    Family.objects.filter(familyID=famObj.familyID).update(currentCount=temp)


class Family(models.Model):
    surveyID = models.ForeignKey(
        SurveyList, blank=True, null=True, on_delete=models.CASCADE, related_name='hhs_surveys')
    collegeID = models.ForeignKey(
        CollegeList, blank=True, null=True, on_delete=models.CASCADE, related_name='families')
    familyID = models.AutoField(primary_key=True, verbose_name='Family ID')
    noOfMembers = models.IntegerField(default=0, verbose_name='No. of Members')
    currentCount = models.IntegerField(default=0)
    noOfCars = models.IntegerField(default=0, verbose_name='No. of Cars')
    noOfCycles = models.IntegerField(default=0, verbose_name='No. of Cycles')
    noOfTwoWheelers = models.IntegerField(
        default=0, verbose_name='No. of Two Wheelers')
    familyIncome = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Family Income')
    country = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Country')
    homeState = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Home State')
    landmark = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Landmark')
    lat = models.CharField(max_length=100, blank=True,
                           null=True, verbose_name='Latitude')
    lng = models.CharField(max_length=100, blank=True,
                           null=True, verbose_name='Longitude')
    nameOfDistrict = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="District")

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "Families"

    # def __str__(self):
        # return str(self.memberID)


class Member(models.Model):
    memberID = models.AutoField(primary_key=True, verbose_name='Member ID')
    familyID = models.ForeignKey(
        Family, blank=True, null=True, on_delete=models.CASCADE, related_name='members')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Created Time')

    gender = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Gender')
    age = models.CharField(max_length=100, null=True,
                           blank=True, verbose_name='Age')
    educationalQualification = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Educational Qualifications')
    monthlyIncome = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Monthly Income')
    maritialStatus = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Marital Status')
    differentlyAbled = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Differently Abled')
    principalSourceofIncome = models.CharField(
        max_length=300, null=True, blank=True, verbose_name='Principal Source of Income')
    stayAtHome = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Stay at Home')
    householdHead = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Household Head')
    respondent = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Respondent')
    twoWheelerLicense = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Two Wheeler License')
    simCards = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Sim Cards')
    fourWheelerLicense = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Four Wheeler License')
    dataWhileDriving = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Data While Driving')
    bluetooth = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Bluetooth')
    wifi = models.CharField(max_length=100, blank=True,
                            null=True, verbose_name='WiFi')
    # district = models.CharField(max_length=100, blank=True, null=True, verbose_name='District')

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "Members"

    def __str__(self):
        return str(self.memberID)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Product.
        """
        return reverse('member-view', args=[str(self.memberID)])


post_save.connect(updateCurrentCount, sender=Member)


class Trip(models.Model):
    tripID = models.AutoField(primary_key=True, verbose_name='Trip ID')
    memberID = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='trips', verbose_name='Member ID')

    def __str__(self):
        return str(self.tripID)

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "Trips"


class MemberDistrict(models.Model):
    memberDistrictId = models.AutoField(
        primary_key=True, verbose_name='Member District ID')
    memberDistrict = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Member District')
    memberID = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name='Districts', verbose_name='Member ID')

    def __str__(self):
        return str(self.memberDistrict)

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "MemberDistricts"


class OriginDestination(models.Model):
    tripID = models.ForeignKey(Trip, on_delete=models.CASCADE,
                               related_name='origin_destination', verbose_name='Trip ID')
    originDestinationID = models.AutoField(
        primary_key=True, verbose_name='Origin Destination ID')
    originLandmark = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Origin Landmark')
    originLat = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Origin Latitude')
    originLng = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Origin Longitude')
    originPlace = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Origin Place')
    destinationLandmark = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Destination Landmark')
    destinationLat = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Destination Latitude')
    destinationLng = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Destination Longitude')
    destinationPlace = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Destination Place')
    fare = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name='Fare')
    travelDistance = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Travel Distance')
    # travelTime = models.CharField(max_length=100, null=True, blank=True)
    departureTime = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Departure Time')
    arrivalTime = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Arrival Time')

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "OriginDestinations"


class Mode(models.Model):
    tripID = models.ForeignKey(
        Trip, on_delete=models.CASCADE, related_name='mode_types', verbose_name='Trip ID')
    modeID = models.AutoField(primary_key=True, verbose_name='Mode ID')
    # modeType = models.CharField(max_length=100, null=True, blank=True)
    modeName = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Mode Name')
    modeIndex = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Mode Index')
    # fare = models.CharField(max_length=100, null=True, blank=True)
    # travelDistance = models.CharField(max_length=100, null=True, blank=True)
    # travelTime = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "ModeTypes"
        # abstract = True

    # def __str__(self):
    # 	return self.modeType+' : '+self.accessMode


class Feedback(models.Model):
    feedback = models.TextField(blank=True, null=True, verbose_name='Feedback')
    feedback_time = models.DateTimeField(
        default=timezone.now, verbose_name='Feedback Time')

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "Feedbacks"


class PtSurvey(models.Model):
    surveyID = models.ForeignKey(SurveyList, blank=True, null=True,
                                 on_delete=models.CASCADE, related_name='pt_surveys', verbose_name='Survey ID')
    collegeID = models.ForeignKey(CollegeList, blank=True, null=True,
                                  on_delete=models.CASCADE, related_name='ptSurveys', verbose_name='College ID')
    personID = models.AutoField(primary_key=True, verbose_name='Person ID')

    age = models.CharField(max_length=100, null=True,
                           blank=True, verbose_name='Age')
    gender = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Gender')
    educationalQualification = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Educational Qualifications')
    profession = models.CharField(
        max_length=300, null=True, blank=True, verbose_name='Profession')
    monthlyIncome = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Monthly Income')
    noOfCars = models.IntegerField(default=0, verbose_name='No. of Cars')
    noOfTwoWheelers = models.IntegerField(
        default=0, verbose_name='No. of Two Wheelers')
    noOfCycles = models.IntegerField(default=0, verbose_name='No. of Cycles')

    metro = models.CharField(max_length=100, null=True,
                             blank=True, verbose_name='Metro')

    travelPurpose = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Travel Purpose')
    fromLandmark = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='From Landmark')
    toLandmark = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='To Landmark')
    travelTime = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Travel Time')
    travelCost = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Travel Cost')
    accesMode = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Access Mode')
    egressMode = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Egress Mode')
    travelFreq = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Travel Frequency')

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "PtSurveys"


class PtSurveyRating(models.Model):
    personID = models.ForeignKey(PtSurvey, blank=True, null=True,
                                 on_delete=models.CASCADE, related_name='ptPersons', verbose_name='Person ID')
    ptSurveyRatingId = models.AutoField(
        primary_key=True, verbose_name='PT Survey Rating ID')

    metro = models.CharField(max_length=100, null=True,
                             blank=True, verbose_name='Metro')

    racc1 = models.CharField(max_length=100, null=True, blank=True)
    racc2 = models.CharField(max_length=100, null=True, blank=True)
    racc3 = models.CharField(max_length=100, null=True, blank=True)

    rtrav1 = models.CharField(max_length=100, null=True, blank=True)
    rtrav2 = models.CharField(max_length=100, null=True, blank=True)
    rtrav3 = models.CharField(max_length=100, null=True, blank=True)
    rtrav4 = models.CharField(max_length=100, null=True, blank=True)
    rtrav5 = models.CharField(max_length=100, null=True, blank=True)
    rtrav6 = models.CharField(max_length=100, null=True, blank=True)
    rtrav7 = models.CharField(max_length=100, null=True, blank=True)
    rtrav8 = models.CharField(max_length=100, null=True, blank=True)

    rmov1 = models.CharField(max_length=100, null=True, blank=True)
    rmov2 = models.CharField(max_length=100, null=True, blank=True)
    rmov3 = models.CharField(max_length=100, null=True, blank=True)
    rmov4 = models.CharField(max_length=100, null=True, blank=True)
    rmov5 = models.CharField(max_length=100, null=True, blank=True)
    rmov6 = models.CharField(max_length=100, null=True, blank=True)
    rmov7 = models.CharField(max_length=100, null=True, blank=True)
    rmov8 = models.CharField(max_length=100, null=True, blank=True)
    rmov9 = models.CharField(max_length=100, null=True, blank=True)
    rmov10 = models.CharField(max_length=100, null=True, blank=True)

    rcom1 = models.CharField(max_length=100, null=True, blank=True)
    rcom2 = models.CharField(max_length=100, null=True, blank=True)
    rcom3 = models.CharField(max_length=100, null=True, blank=True)
    rcom4 = models.CharField(max_length=100, null=True, blank=True)
    rcom5 = models.CharField(max_length=100, null=True, blank=True)
    rcom6 = models.CharField(max_length=100, null=True, blank=True)
    rcom7 = models.CharField(max_length=100, null=True, blank=True)
    rcom8 = models.CharField(max_length=100, null=True, blank=True)
    rcom9 = models.CharField(max_length=100, null=True, blank=True)
    rcom10 = models.CharField(max_length=100, null=True, blank=True)

    rsec1 = models.CharField(max_length=100, null=True, blank=True)
    rsec2 = models.CharField(max_length=100, null=True, blank=True)
    rsec3 = models.CharField(max_length=100, null=True, blank=True)
    rsec4 = models.CharField(max_length=100, null=True, blank=True)

    rover1 = models.CharField(max_length=100, null=True, blank=True)
    rover2 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "PtSurveyRatings"


class AQIPerceptionSurvey(models.Model):
    surveyID = models.ForeignKey(SurveyList, blank=True, null=True, on_delete=models.CASCADE,
                                 related_name='aqiPerceptionSurveys', verbose_name='Survey ID')
    collegeID = models.ForeignKey(CollegeList, blank=True, null=True, on_delete=models.CASCADE,
                                  related_name='aqiPerception_Surveys', verbose_name='College ID')
    memberID = models.AutoField(
        primary_key=True, verbose_name='Member or respondent ID')
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name='Created Time')
    # Part A
    homeTehsil = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Home or origin Tehsil')
    existingHealthConditions = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Any existing health issues')
    airPollutionMajorProb = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Air Pollution Major Iusse in locality')
    airPollutionAdverseHealthEffect = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Air Pollution Adverse Health Effect')
    aqiUnderstanding = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='AQI Understanding')
    # UnderstandAbove = models.CharField(max_length=100, null=True, blank=True, verbose_name='Understanding given example')
    airQualityLevelBad = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='AQI perception')
    checkingAirQualityLevel = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='AQI Source')
    fequentlyAirQualityLevel = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='AQI Chcek Frequency')
    # Part B
    destinationTehsil = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Destination Tehsil')
    tripsPerDay = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Trips per day')
    averageTripLengthPrimary = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Average trip length primary trips')
    averageTripLengthSecondary = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Average trip length secondary trips')
    purposeTrip = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Trip purpose')
    primaryTrip = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Travel mode for primary trip')
    secondaryTrip = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Travel mode for secondary trip')
    avoidTrip = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='avoid trip due to Air Poll')
    impactOnPrimaryActs = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Impact on travel choices for primary activities')
    impactOnSecondaryActs = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Impact on travel choices for secondary activities')
    primaryActTripPreference = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Primary activity trip preferences')
    secondaryActTripPreference = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Secondary activity trip preferences')
    reasonNotToChangeChoices = models.CharField(
        max_length=500, null=True, blank=True, verbose_name='Reason for not changing the travel choice due to poor AQ')
    # Part E
    informationRequired = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='need of information')
    avoidWalk = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='avoid walk in air poll')
    primaryActTripPreferenceAQIAPI = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Primary activity trip preferences for AQI API')
    secondaryActTripPreferenceAQIAPI = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Secondary activity trip preferences  for AQI API')
    primaryModeAQIAPI = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Primary activity travel mode  for AQI API')
    secondaryModeAQIAPI = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Secondary activity travel mode for AQI API')
    # Part C
    perceiveAQIHome = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='AQI at home')
    perceiveAQIWork = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='AQI at work')
    healthEffect = models.CharField(
        max_length=600, null=True, blank=True, verbose_name='Impact on health')
    familyHealthEffect = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Impact on family health')
    travelHealthEffect = models.CharField(
        max_length=300, null=True, blank=True, verbose_name='Impact on health while traveling')
    sensitiveGroupEffect = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Impact of poor AQI on sensitive age-groups')
    psychologyEffect = models.CharField(
        max_length=300, null=True, blank=True, verbose_name='psychological effect')
    # Part D
    maskAirPollution = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='use of mask air poll')
    airFilter = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='use of air filter')
    missSchool = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='avoid school due to air poll')
    # closeWindow = models.CharField(max_length=100, null=True, blank=True, verbose_name='keeping windows closed')
    outdoorActivity = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='no outdoor activites')
    # Part F
    age = models.CharField(max_length=100, null=True,
                           blank=True, verbose_name='Age')
    gender = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Gender')
    educationalQualification = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Educational Qualifications')
    noOfCars = models.IntegerField(default=0, verbose_name='No. of Cars')
    noOfTwoWheelers = models.IntegerField(
        default=0, verbose_name='No. of Two Wheelers')
    noOfCycles = models.IntegerField(default=0, verbose_name='No. of Cycles')
    monthlyIncome = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Monthly Income')
    maritialStatus = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Marital Status')
    profession = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Profession')
    comment = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Comment')

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "AqiPerceptionSurveys"


class TableWillingnessSurveyDetails(models.Model):
    PurposeOfDailyTrip = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='PurposeOfDailyTrip')
    BoardingFrom = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='BoardingFrom')
    Alighting = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Alighting')
    TimeOfBoarding = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='TimeOfBoarding')
    ApproximateTime = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ApproximateTime')
    TravelCost = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='TravelCost')

    NumberOfTrip = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='NumberOfTrip')
    levelOfCrowding = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='levelOfCrowding')
    currentlevelofCrowding = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='currentlevelofCrowding')
    CrowdingBecomeUncomfortable = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='CrowdingBecomeUncomfortable')
    GaugeCrowding = ArrayField(models.CharField(max_length=100),
                               max_length=100,   default=list, null=True, blank=True, verbose_name='GaugeCrowding')
    CrowdingAffectYourMood = ArrayField(models.CharField(max_length=100),
                                        max_length=100, default=list, null=True, blank=True, verbose_name='CrowdingAffectYourMood')
    ChangeModeOfTransport = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChangeModeOfTransport')

# CHOICE SET A
    ChoiceSetOneTravelTimeAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetOneTravelTimeAltA')
    ChoiceSetOneSingleTicketTripAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetOneSingleTicketTripAltA')
    ChoiceSetOnePositionAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetOnePositionAltA')
    ChoiceSetOnePepoleStandingAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetOnePepoleStandingAltA')
# CHOICE SET B
    ChoiceSetOneTravelTimeAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetOneTravelTimeAltB')
    ChoiceSetOneSingleTicketTripAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetOneSingleTicketTripAltB')
    ChoiceSetOnePositionAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetOnePositionAltB')
    ChoiceSetOnePepoleStandingAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetOnePepoleStandingAltB')
    ChoiceSetOneOption = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetOneOption')

# OPTION 2 CHOICE SET A
    ChoiceSetTwoTravelTimeAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetTwoTravelTimeAltA')
    ChoiceSetTwoSingleTicketTripAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetTwoSingleTicketTripAltA')
    ChoiceSetTwoPositionAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetTwoPositionAltA')
    ChoiceSetTwoPepoleStandingAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetTwoPepoleStandingAltA')


# OPTION 2 CHOICE SET B
    ChoiceSetTwoTravelTimeAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetTwoTravelTimeAltA')
    ChoiceSetTwoSingleTicketTripAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetTwoSingleTicketTripAltA')
    ChoiceSetTwoPositionAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetTwoPositionAltA')
    ChoiceSetTwoPepoleStandingAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetTwoPepoleStandingAltA')
    ChoiceSetTwoOption = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetTwoOption')

# OPTION 3 CHOICE SET A

    ChoiceSetThreeTravelTimeAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetThreeTravelTimeAltA')
    ChoiceSetThreeSingleTicketTripAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetThreeSingleTicketTripAltA')
    ChoiceSetThreePositionAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetThreePositionAltA')
    ChoiceSetThreePepoleStandingAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetThreePepoleStandingAltA')

# OPTION 3 CHOICE SET B
    ChoiceSetThreeTravelTimeAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetThreeTravelTimeAltB')
    ChoiceSetThreeSingleTicketTripAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetThreeSingleTicketTripAltB')
    ChoiceSetThreePositionAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetThreePositionAltB')
    ChoiceSetThreePepoleStandingAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetThreePepoleStandingAltB')
    ChoiceSetThreeOption = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetThreeOption')


# OPTION 4 CHOICE SET A

    ChoiceSetFourTravelTimeAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetFourTravelTimeAltA')
    ChoiceSetFourSingleTicketTripAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetFourSingleTicketTripAltA')
    ChoiceSetFourPositionAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetFourPositionAltA')
    ChoiceSetFourPepoleStandingAltA = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetFourPepoleStandingAltA')
# OPTION 4 CHOICE SET B
    ChoiceSetFourTravelTimeAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetFourTravelTimeAltB')
    ChoiceSetFourSingleTicketTripAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetFourSingleTicketTripAltB')
    ChoiceSetFourPositionAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetFourPositionAltB')
    ChoiceSetFourPepoleStandingAltB = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetFourPepoleStandingAltB')
    ChoiceSetFourOption = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChoiceSetFourOption')

    Payapremium = ArrayField(models.CharField(max_length=100),
                             max_length=100, null=True, blank=True, verbose_name='Payapremium')
    Alternatetransport = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Alternatetransport')

    # PAGE -4
    Gender = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Gender')
    Age = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Age')
    Qualification = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Qualification')
    Occupation = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Occupation')
    MonthlyHouseHoldIncome = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='MonthlyHouseHoldIncome')
    DrivingLicense = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='DrivingLicense')
    SelectedOwnershipBycycle = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='SelectedOwnershipBycycle')
    SelectedOwnershipBike = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='SelectedOwnershipBike')
    SelectedOwnershipCar = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='SelectedOwnershipCar')

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "TableWillingnessSurveyDetails"


class TableUnwilligness(models.Model):
    PurposeOfDailyTrip = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='PurposeOfDailyTrip')
    SameTravelMode = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='SameTravelMode')
    TimeOfBoarding = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='TimeOfBoarding')
    ApproximateTime = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ApproximateTime')
    TravelCost = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='TravelCost')
    NumberOfTransferInJourney = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='TravelCost')
    CrowdingBecomeUncomfortable = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='CrowdingBecomeUncomfortable')
    levelOfCrowding = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='levelOfCrowding')
    currentlevelofCrowding = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='currentlevelofCrowding')
    GaugeCrowding = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='GaugeCrowding')
    CrowdingAffectYourMood = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='CrowdingAffectYourMood')
    ChangeModeOfTransport = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='ChangeModeOfTransport')
    # _________-this is for the third section ---------------------------------------------###
    Gender = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Gender')
    Age = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Age')
    Qualification = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Qualification')
    Occupation = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Occupation')
    MonthlyHouseHoldIncome = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='MonthlyHouseHoldIncome')
    DrivingLicense = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='DrivingLicense')
    SelectedOwnership = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='SelectedOwnership')


class TabletravelDetalis(models.Model):
    alt1_TravelTime = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Alt1_TravelTime')
    alt1_TravelCost = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Alt1_TravelCost'
    )
    alt1_Standing = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Alt1_Standing'
    )
    alt1_Crowding = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Alt1_Crowding'
    )
    alt2_TravelTime = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Alt2_TravelTime'
    )
    alt2_TravelCost = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Alt2_TravelCost'
    )
    alt2_Standing = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Alt2_Standing'
    )
    alt2_Crowding = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Alt2_Crowding'
    )
    used = models.CharField(
        max_length=100, null=True, blank=True, verbose_name='Used'
    )
    table_used_number = models.CharField(
        max_length=3, null=True, blank=True, verbose_name='Table_used_number'
    )

    class Meta:
        app_label = "transdb"
        verbose_name_plural = "TabletravelDetalis"
