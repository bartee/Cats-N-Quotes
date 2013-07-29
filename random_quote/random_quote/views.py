__author__ = 'bartstroeken'


from quotes.models import Quote, BackgroundImage
from random import random
from django.views.generic.base import TemplateView
from quotes.util import CachedRandomPicker

class HomeView(TemplateView):
    """
    Get and render a random quote, and a button to refresh it.
    """
    template_name = 'random_quote.html'

    def get_context_data(self, **kwargs):
        """
        Get a random quote, and put it in the context

        """

        quote_ids = Quote.objects.all().values('id')

        quote_random_picker = CachedRandomPicker([item.get('id') for item in quote_ids], 'random_quotes', 0.2)
        quote = Quote.objects.get(pk=quote_random_picker.random())

        tags = quote.tags.all()

        all_background_ids = BackgroundImage.objects.all().values('id')
        background_random_picker = CachedRandomPicker([item.get('id') for item in all_background_ids],'background_ids')

        # Background selection
        if len(tags) > 0:
            background_ids = BackgroundImage.objects.filter(tags__in=tags).values('id')
            background = background_random_picker.random_from_subset([item.get('id') for item in background_ids])
        else:
            background = background_random_picker.random()
        background = BackgroundImage.objects.get(pk=background)

        context = super(HomeView,self).get_context_data(**kwargs)
        context['quote'] = quote
        context['background_image'] = background.url

        return context
