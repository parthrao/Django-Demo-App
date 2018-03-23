from django.db import models
from django.core.urlresolvers import  reverse

# Create your models here.
class File(models.Model):
	name = models.CharField(max_length=250)
	file_title = models.CharField(max_length=500)
	company = models.CharField(max_length=100)
	file_url = models.FileField()
	file_type = models.CharField(max_length=100)
	# file_actual =  models.FileField()

	def get_absolute_url(self):
		return reverse('uploadfile:index')
		
	def __str__(self):
		return self.name + ' - ' + self.company 

