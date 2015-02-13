from django.conf.urls import patterns, url

from qna import views

urlpatterns = patterns('',
	url(r'^tags/$', views.tags, name='tags'),
	#url(r'^$', views.askq, name='askq'),
	url(r'^$', views.tags, name='tags'),
	url(r'^tags/(?P<tag>[a-zA-Z_ ]+)', views.qfortag, name='qfortag'),
	url(r'image/(?P<image>[a-zA-Z.]+)',views.images, name='images'),
)


