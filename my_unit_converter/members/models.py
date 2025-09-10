from django.db import models

class Member(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	phone = models.IntegerField(null=True)
	joined_date = models.DateField(null=True)


# Create your models here.
class UnitInformation(models.Model):
	fromUnit = models.CharField(max_length=255)
	toUnit = models.CharField(max_length=255)
	unitAmount = models.DecimalField(decimal_places=3, max_digits=7)