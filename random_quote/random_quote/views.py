__author__ = 'bartstroeken'


from quotes.models import Quote, BackgroundImage
from random import choice
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

        context = super(HomeView,self).get_context_data(**kwargs)

        number_of_records = Quote.objects.all().values('id')
        random_index = choice(number_of_records).get('id')
        quote = Quote.objects.get(pk=random_index)

        if quote.meme is not None:
            self.template_name = 'random_meme_quote.html'
            context['meme'] = quote.meme.image
        else:
            # Background
            number_of_records = BackgroundImage.objects.all().values('id')
            random_index = choice(number_of_records).get('id')
            background = BackgroundImage.objects.get(pk=random_index)
            context['background_image'] = background.url

        context['quote'] = quote

        return context
