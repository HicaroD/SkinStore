from django.db import models

class Product(models.Model):
	category = models.CharField(max_length=10, null=True)
	name = models.CharField(max_length=40, null=True)
	quality = models.CharField(max_length=40, null=True)
	price = models.FloatField()
	primary_image_url = models.CharField(null=True, max_length=50)	
	secondary_image_url = models.CharField(null=True, max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["-price"]