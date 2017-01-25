from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login$', views.index),
	url(r'^login/register$', views.register),
	url(r'^login/login$', views.login)
]