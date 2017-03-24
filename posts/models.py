from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to="post_images/%Y/%m/%d", null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title