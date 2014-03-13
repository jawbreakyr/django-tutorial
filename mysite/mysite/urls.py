from django.conf.urls import patterns, include, url
from django.contrib import admin

from generic.views import HomeView

admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name="home"),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
