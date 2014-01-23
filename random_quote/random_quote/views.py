__author__ = 'bartstroeken'


from quotes.models import Quote, BackgroundImage
from django.views.generic.base import TemplateView
from quotes.util import CachedRandomPicker
from quotes.views import QuoteView
from random import choice, random

class HomeView(QuoteView):

    """
    Get and render a random quote, and a button to refresh it.
    """
    template_name = 'detail_quote.html'

    def get_context_data(self, **kwargs):
        """
        Get a random quote, and put it in the context

        """
        quote_ids = Quote.objects.all().values('id')

        quote_random_picker = CachedRandomPicker([item.get('id') for item in quote_ids], 'random_quotes', 0.2)
        quote = Quote.objects.get(pk=quote_random_picker.random())

        kwargs = {'quote':quote}

        return super(HomeView, self).get_context_data(**kwargs)
