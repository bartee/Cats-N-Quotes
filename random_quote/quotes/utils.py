__author__ = 'andrewgerssen'

from django.core.urlresolvers import reverse

def url(viewname, *args, **kwargs):
    """Return URL using django's ``reverse()`` function."""
    return reverse(viewname, args=args, kwargs=kwargs)