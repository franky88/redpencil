from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def postIndex(request):
	post_list = Post.objects.all().order_by("-timestamp", "-updated")
	context = {
		"title": "post grid",
		"postlist": post_list,
	}
	return render(request, "posts/posts_index.html", context)

def postDetail(request, pk):
	post_instance = get_object_or_404(Post, pk=pk)
	context = {
		"title": "post detail",
		"postinstance": post_instance,
	}
	return render(request, "posts/posts_detail.html", context)