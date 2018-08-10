from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sample/process$', views.process),
    url(r'^results$', views.results),
	url(r'^back$', views.back)
]
