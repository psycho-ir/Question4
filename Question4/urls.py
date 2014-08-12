from django.conf.urls import patterns, include, url

from django.contrib import admin
from ws_client.views import ShowIPView, IPServiceView, LoginView

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Question4.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^(?i)service/ip/(?P<session_id>.*)/(?P<ip_address>.*)', IPServiceView.as_view()),
                       url(r'^(?i)service/login/(?P<username>.*)/(?P<password>.*)', LoginView.as_view()),
                       url(r'', ShowIPView.as_view()),
)
