from django.conf.urls import patterns, url
from views import QuoteView, AuthorView

urlpatterns = patterns('',
    url(r'^quote/(?P<id>[0-9]+)$', QuoteView.as_view(), name='detail'),
    url(r'^author/(?P<author_name>[a-zA-Z0-9]+)$', AuthorView.as_view(), name='author_quotes'),
)
