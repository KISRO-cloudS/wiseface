from django.db import models

class Donation(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=400)
	amount = models.DecimalField(max_digits=3, decimal_places=2)
