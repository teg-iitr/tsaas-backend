from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

class TransDB(models.Model):
	memberId = models.AutoField(primary_key=True)
	# Family = models.ForeignKey("FamilyDB", blank=True, null=True)
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

	# def __str__(self):
		# return self.Member_ID

class FamilyDB(models.Model):
	Family_ID = models.IntegerField(primary_key=True)
