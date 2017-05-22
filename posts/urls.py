from django.conf.urls import url
from . import views

app_name = "posts"
urlpatterns = [
    url(r'^$', views.postIndex, name="index"),
    url(r'^addpost/$', views.addPost, name="addpost"),
    url(r'^details/(?P<pk>[0-9]+)/$', views.postDetail, name="detail"),
    url(r'^category/(?P<pk>[0-9]+)/$', views.postCatDetail, name="catdetail"),
]