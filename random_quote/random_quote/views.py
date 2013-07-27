__author__ = 'bartstroeken'


from quotes.models import Quote, BackgroundImage
from random import random
from django.views.generic.base import TemplateView

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
        from random import choice, randint
        random_index = choice(quote_ids).get('id')
        quote = Quote.objects.get(pk=random_index)
        tags = quote.tags.all()

        # Background
        if len(tags) > 0:
            background_ids = BackgroundImage.objects.filter(tags__in=tags).values('id')
        else:
            background_ids = BackgroundImage.objects.all().values('id')

        random_index = choice(background_ids).get('id')
        background = BackgroundImage.objects.get(pk=random_index)

        context = super(HomeView,self).get_context_data(**kwargs)
        context['quote'] = quote
        context['background_image'] = background.url

        return context
