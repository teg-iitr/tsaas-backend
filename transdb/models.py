from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models.signals import post_save
from django.db.models import Subquery, OuterRef


# Create your models here.

def create_surveyStartTimeAndSurveyEndTime(sender, **kwargs): 
	if kwargs.get('created', False): 
		ResponseTime.objects.get_or_create(
			surveyID=kwargs.get('instance'),
			responseTimeID=kwargs.get('instance').surveyID
		)

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
	surveyID = models.ForeignKey(SurveyList, blank=True, null=True, on_delete=models.CASCADE, related_name='surveyResponseTime')
	

	class Meta:
		app_label = "transdb"
		verbose_name_plural = "ResponseTimes"

class CollegeList(models.Model):
	collegeID = models.AutoField(primary_key=True)
	collegeName = models.CharField(max_length=100, default="")
	collegeURL = models.SlugField(unique=True)
	constrainField = models.CharField(max_length=100, null=True, blank=True)
	surveyTypeID = models.ForeignKey(SurveyType, blank=True, null=True, on_delete=models.CASCADE, related_name='surveyType')
	
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
	Family.objects.filter(familyID=famObj.familyID).update(currentCount = temp)

class Family(models.Model):
	surveyID = models.ForeignKey(SurveyList, blank=True, null=True, on_delete=models.CASCADE, related_name='hhs_surveys')
	collegeID = models.ForeignKey(CollegeList, blank=True, null=True, on_delete=models.CASCADE, related_name='families')
	familyID = models.AutoField(primary_key=True)
	noOfMembers = models.IntegerField(default=0)
	currentCount = models.IntegerField(default=0)
	noOfCars = models.IntegerField(default=0)
	noOfCycles = models.IntegerField(default=0)
	noOfTwoWheelers = models.IntegerField(default=0)
	familyIncome = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, null=True, blank=True)
	homeState = models.CharField(max_length=100, null=True, blank=True)
	landmark = models.CharField(max_length=200, null=True, blank=True)
	lat = models.CharField(max_length=100, blank=True, null=True)
	lng = models.CharField(max_length=100, blank=True, null=True)
	nameOfDistrict = models.CharField(max_length=100, null=True, blank=True)

	class Meta:
		app_label = "transdb"
		verbose_name_plural = "Families"

	# def __str__(self):
		# return str(self.memberID)


class Member(models.Model):
	memberID = models.AutoField(primary_key=True)
	familyID = models.ForeignKey(Family, blank=True, null=True, on_delete=models.CASCADE, related_name='members')
	created_at = models.DateTimeField(default=timezone.now)
	
	gender = models.CharField(max_length=100, null=True, blank=True)
	age = models.CharField(max_length=100, null=True, blank=True)
	educationalQualification = models.CharField(max_length=100, null=True, blank=True)
	monthlyIncome = models.CharField(max_length=100, null=True, blank=True)
	maritialStatus = models.CharField(max_length=100, null=True, blank=True)
	differentlyAbled = models.CharField(max_length=100, null=True, blank=True)
	principalSourceofIncome = models.CharField(max_length=300, null=True, blank=True)
	stayAtHome = models.CharField(max_length=100, blank=True, null=True)
	householdHead = models.CharField(max_length=100, blank=True, null=True)
	respondent = models.CharField(max_length=100, blank=True, null=True)
	twoWheelerLicense = models.CharField(max_length=100, blank=True, null=True)
	simCards = models.CharField(max_length=100, blank=True, null=True)
	fourWheelerLicense = models.CharField(max_length=100, blank=True, null=True)
	dataWhileDriving = models.CharField(max_length=100, blank=True, null=True)
	bluetooth = models.CharField(max_length=100, blank=True, null=True)
	wifi = models.CharField(max_length=100, blank=True, null=True)

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
	tripID = models.AutoField(primary_key=True)
	memberID = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='trips')
	def __str__(self):
		return str(self.tripID)

	class Meta:
		app_label = "transdb"
		verbose_name_plural = "Trips"

class OriginDestination(models.Model):
	tripID = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='origin_destination')
	originDestinationID = models.AutoField(primary_key=True)
	originLandmark = models.CharField(max_length=100, null=True, blank=True)
	originLat = models.CharField(max_length=100, null=True, blank=True)
	originLng = models.CharField(max_length=100, null=True, blank=True)
	originPlace = models.CharField(max_length=100, null=True, blank=True)
	destinationLandmark = models.CharField(max_length=100, null=True, blank=True)
	destinationLat = models.CharField(max_length=100, null=True, blank=True)
	destinationLng = models.CharField(max_length=100, null=True, blank=True)
	destinationPlace = models.CharField(max_length=100, null=True, blank=True)
	fare = models.CharField(max_length=100, null=True, blank=True)
	travelDistance = models.CharField(max_length=100, null=True, blank=True)
	# travelTime = models.CharField(max_length=100, null=True, blank=True)
	departureTime= models.CharField(max_length=100, null=True, blank=True)
	arrivalTime= models.CharField(max_length=100, null=True, blank=True)

	class Meta:
		app_label = "transdb"
		verbose_name_plural = "OriginDestinations"


class Mode(models.Model):
	tripID = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='mode_types')
	modeID = models.AutoField(primary_key=True)
	# modeType = models.CharField(max_length=100, null=True, blank=True)
	modeName = models.CharField(max_length=100, null=True, blank=True)
	modeIndex = models.CharField(max_length=100, null=True, blank=True)
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
	feedback = models.TextField(blank=True, null=True)
	feedback_time = models.DateTimeField(default=timezone.now)

	class Meta:
		app_label = "transdb"
		verbose_name_plural = "Feedbacks"


class PtSurvey(models.Model):
	surveyID = models.ForeignKey(SurveyList, blank=True, null=True, on_delete=models.CASCADE, related_name='pt_surveys')
	collegeID = models.ForeignKey(CollegeList, blank=True, null=True, on_delete=models.CASCADE, related_name='ptSurveys')
	personID = models.AutoField(primary_key=True)
	
	age = models.CharField(max_length=100, null=True, blank=True)
	gender = models.CharField(max_length=100, null=True, blank=True)
	educationalQualification = models.CharField(max_length=100, null=True, blank=True)
	profession = models.CharField(max_length=300, null=True, blank=True)
	monthlyIncome = models.CharField(max_length=100, null=True, blank=True)
	noOfCars = models.IntegerField(default=0)
	noOfTwoWheelers = models.IntegerField(default=0)
	noOfCycles = models.IntegerField(default=0)
	
	metro = models.CharField(max_length=100, null=True, blank=True)

	travelPurpose = models.CharField(max_length=100, null=True, blank=True)
	fromLandmark = models.CharField(max_length=200, null=True, blank=True)
	toLandmark = models.CharField(max_length=200, null=True, blank=True)
	travelTime = models.CharField(max_length=200, null=True, blank=True)
	travelCost = models.CharField(max_length=200, null=True, blank=True)
	accesMode = models.CharField(max_length=200, null=True, blank=True)
	egressMode = models.CharField(max_length=200, null=True, blank=True)
	travelFreq = models.CharField(max_length=200, null=True, blank=True)

	class Meta:
		app_label = "transdb"
		verbose_name_plural = "PtSurveys"


class PtSurveyRating(models.Model):
	personID = models.ForeignKey(PtSurvey, blank=True, null=True, on_delete=models.CASCADE, related_name='ptPersons')
	ptSurveyRatingId = models.AutoField(primary_key=True)

	metro = models.CharField(max_length=100, null=True, blank=True)
	
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
