from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def postIndex(request):
	cat_list = Category.objects.all()
	post_list = Post.objects.all().order_by("-timestamp", "-updated")
	context = {
		"title": "all post",
		"postlist": post_list,
		"catlist": cat_list,
	}
	return render(request, "posts/posts_index.html", context)

def postDetail(request, pk):
	post_instance = get_object_or_404(Post, pk=pk)
	context = {
		"title": "post detail",
		"postinstance": post_instance,
	}
	return render(request, "posts/posts_detail.html", context)

def postCatDetail(request, pk):
	cat_list = Category.objects.all()
	cat_instance = get_object_or_404(Category, pk=pk)
	context = {
		"title": "category",
		"catlist": cat_list,
		"catinstance": cat_instance,
	}
	return render(request, "posts/posts_category_detail.html", context)