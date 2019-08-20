from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

class SurveyList(models.Model):
	surveyID = models.IntegerField(primary_key=True)
	surveyType = models.CharField(max_length=100, null=True, blank=True)

class SurveyStartTime(models.Model):
	surveyStartTimeID = models.IntegerField(primary_key=True)
	surveyID = models.ForeignKey(SurveyList, blank=True, null=True, on_delete=models.CASCADE, related_name='surveyStartTime')

class SurveyEndTime(models.Model):
	surveyEndTimeID = models.IntegerField(primary_key=True)
	surveyID = models.ForeignKey(SurveyList, blank=True, null=True, on_delete=models.CASCADE, related_name='surveyEndTime')

class CollegeList(models.Model):
	collegeID = models.AutoField(primary_key=True)
	collegeName = models.CharField(max_length=100, default="")
	collegeURL = models.SlugField(unique=True)

	class Meta:
		app_label = "transdb"
		verbose_name_plural = "College List"

	def __str__(self):
		return str(self.collegeName)
	# def get_absolute_url(self):
	# 	return reverse(kwargs={'slug': self.collegeURL})


class Family(models.Model):
	collegeID = models.ForeignKey(CollegeList, blank=True, null=True, on_delete=models.CASCADE, related_name='families')
	familyID = models.AutoField(primary_key=True)
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
	travelTime = models.CharField(max_length=100, null=True, blank=True)


	class Meta:
		app_label = "transdb"
		verbose_name_plural = "Origin Destination"


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
		verbose_name_plural = "Mode Type"
		# abstract = True

	# def __str__(self):
	# 	return self.modeType+' : '+self.accessMode

class Feedback(models.Model):
	feedback = models.TextField(blank=True, null=True)
	feedback_time = models.DateTimeField(default=timezone.now)

	class Meta:
		app_label = "transdb"
		verbose_name_plural = "Feedbacks"