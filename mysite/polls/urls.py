from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	# turned a simple views.vote to cammeltoe pass to as_view() function
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
   	url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name='results'),
  	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)views