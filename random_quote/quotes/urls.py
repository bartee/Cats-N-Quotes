from django.conf.urls import patterns, url
from views import DetailView

urlpatterns = patterns('',
    url(r'^quote/(?P<id>[0-9]+)$', DetailView.as_view(), name='detail'),
)
