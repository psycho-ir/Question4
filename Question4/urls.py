from django.conf.urls import patterns, include, url

from django.contrib import admin
from ws_client.views import ShowIPView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Question4.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', ShowIPView.as_view()),
)
