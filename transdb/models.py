from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

class Family(models.Model):
	familyID = models.AutoField(primary_key=True)

	class Meta:
		verbose_name_plural = "Families"

class Member(models.Model):
	memberID = models.AutoField(primary_key=True)
	familyID = models.ForeignKey(Family, blank=True, null=True, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)
	gender = models.CharField(max_length=100, null=True, blank=True)
	age = models.CharField(max_length=100, null=True, blank=True)
	educationalQualification = models.CharField(max_length=100, null=True, blank=True)
	monthlyIncome = models.CharField(max_length=100, null=True, blank=True)
	maritialStatus = models.CharField(max_length=100, null=True, blank=True)
	differentlyAbled = models.CharField(max_length=100, null=True, blank=True)
	homeState = models.CharField(max_length=100, null=True, blank=True)
	nameOfDistrict = models.CharField(max_length=100, null=True, blank=True)
	landmark = models.CharField(max_length=200, null=True, blank=True)
	pincode = models.CharField(max_length=100, null=True, blank=True)	
	principalSourceofIncome = models.CharField(max_length=300, null=True, blank=True)

	class Meta:
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
	memberID = models.ForeignKey(Member, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.tripID)

	class Meta:
		verbose_name_plural = "Trips"

class OriginDestination(models.Model):
	tripID = models.ForeignKey(Trip, on_delete=models.CASCADE)
	originDestinationID = models.AutoField(primary_key=True)
	originLat = models.CharField(max_length=100, null=True, blank=True)
	originLng = models.CharField(max_length=100, null=True, blank=True)
	originPlace = models.CharField(max_length=100, null=True, blank=True)
	destinationLat = models.CharField(max_length=100, null=True, blank=True)
	destinationLng = models.CharField(max_length=100, null=True, blank=True)
	destinationPlace = models.CharField(max_length=100, null=True, blank=True)

	class Meta:
		verbose_name_plural = "Origin Destination"


class Mode(models.Model):
	tripID = models.ForeignKey(Trip, on_delete=models.CASCADE)
	modeID = models.AutoField(primary_key=True)
	modeType = models.CharField(max_length=100, null=True, blank=True)
	accessMode = models.CharField(max_length=100, null=True, blank=True)
	cost = models.CharField(max_length=100, null=True, blank=True)
	fare = models.CharField(max_length=100, null=True, blank=True)
	travelDistance = models.CharField(max_length=100, null=True, blank=True)
	travelTime = models.CharField(max_length=100, null=True, blank=True)

	class Meta:
		verbose_name_plural = "Mode Type"

	def __str__(self):
		return self.modeType+' : '+self.accessMode
