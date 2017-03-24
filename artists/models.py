from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ArtistAddInfo(models.Model):
	artist = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	image = models.ImageField(upload_to="artist_photo/%Y/%m/%d", null=True, blank=True)
	def __unicode__(self):
		return self.artist
	def __str__(self):
		return self.artist.get_full_name()
