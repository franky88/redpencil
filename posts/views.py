from django.shortcuts import render
from .models import Post
# Create your views here.
def postIndex(request):
	post_list = models.ForiegnKey(Post, on_delete=models.CASCADE)