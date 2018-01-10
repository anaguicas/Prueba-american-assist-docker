from django.db import models

# Create your models here.
class Country(models.Model):
	
	name = models.CharField('Name', max_length=100)
	code = models.CharField('Code', max_length=3)

	class Meta:
		verbose_name = "Country"
		verbose_name_plural = "Countries"

	def __str__(self):
		return '{} {}'.format(self.name, self.code)
