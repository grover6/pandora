from django.conf.urls import patterns, include, url
from qna2project import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qna2project.views.home', name='home'),
    # url(r'^qna2project/', include('qna2project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^qna/', include('qna.urls')),
	url(r'^$', 'qna.views.tags'),
	#url(r'^media/(?P<image>.*)$',{'document_root':settings.MEDIA_ROOT}),
)
