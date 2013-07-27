__author__ = 'bartstroeken'


from quotes.models import Quote, BackgroundImage
from quotes.views import QuoteView
from random import choice

class HomeView(QuoteView):
    """
    Get and render a random quote, and a button to refresh it.
    """
    template_name = 'random_quote.html'

    def get_context_data(self, **kwargs):
        """
        Get a random quote, and put it in the context

        """

        number_of_records = Quote.objects.all().values('id')
        random_index = choice(number_of_records).get('id')

        return super(HomeView, self).get_context_data(id=random_index)
