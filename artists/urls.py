from django.conf.urls import url
from . import views

app_name = "artists"
urlpatterns = [
    url(r'^$', views.artistIndex, name="index"),
    url(r'^details/(?P<pk>[0-9]+)/$', views.artistDetail, name="detail"),
]