from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to="post_images/%Y/%m/%d", null=True, blank=True)
	def __unicode__(self):
		return self.title