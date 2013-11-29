from django.conf.urls import patterns, url
from views import QuoteView

urlpatterns = patterns('',
    url(r'^quote/(?P<id>[0-9]+)$', QuoteView.as_view(), name='detail'),
)
