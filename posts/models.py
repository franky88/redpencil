from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
	class Meta:
		verbose_name_plural = "categories"
	cat_name = models.CharField(max_length=120, verbose_name="category name")
	def __unicode__(self):
		return self.cat_name
	def __str__(self):
		return self.cat_name
		
class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to="post_images/%Y/%m/%d", null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title