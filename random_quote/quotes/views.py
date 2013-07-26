__author__ = 'Andrew Gerssen'

from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from models import Quote, BackgroundImage

class DetailView(TemplateView):
    """
    Get and render a random quote, and a button to refresh it.
    """
    template_name = 'detail_quote.html'

    def get_context_data(self, **kwargs):
        """
        Get a random quote, and put it in the context

        """
        context = super(DetailView, self).get_context_data(**kwargs)

        quote = get_object_or_404(Quote, pk=self.id)

        # Background
        number_of_records = BackgroundImage.objects.all().values('id')
        from random import choice
        random_index = choice(number_of_records).get('id')
        background = BackgroundImage.objects.get(pk=random_index)

        context['quote'] = quote
        context['background_image'] = background.url

        return context
