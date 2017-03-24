from django.shortcuts import render, get_object_or_404
from .models import ArtistAddInfo
from django.contrib.auth.models import User
# Create your views here.
def artistIndex(request):
	artist_list = User.objects.all()
	context = {
		"title": "artist list",
		"artistlist": artist_list,
	}
	return render(request, "artists/artists_index.html", context)

def artistDetail(request, pk):
	instance = get_object_or_404(User, pk=pk)
	context = {
		"title": "artist detail",
		"instance": instance,
	}
	return render(request, "artists/artists_detail.html", context)