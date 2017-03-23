from django.shortcuts import render
from .models import Post
# Create your views here.
def postIndex(request):
	post_list = Post.objects.all().order_by("-timestamp", "-updated")
	context = {
		"title": "post list",
		"postlist": post_list,
	}
	return render(request, "posts/posts_index.html", context)