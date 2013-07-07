__author__ = 'bartstroeken'


from quotes.models import Quote
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

        number_of_records = Quote.objects.count()
        random_index = int(random()*number_of_records)+1
        quote = Quote.objects.get(pk=random_index)


        context = super(HomeView,self).get_context_data(**kwargs)
        context['quote'] = quote
        context['background_image'] = 'http://lorempixel.com/1000/500/cats/'
        return context
