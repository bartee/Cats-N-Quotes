__author__ = 'Andrew Gerssen'

from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from quotes.util import CachedRandomPicker
from models import Quote, BackgroundImage
from django.core.urlresolvers import reverse
from random import choice

class QuoteView(TemplateView):
    """
    Get and render a random quote, and a button to refresh it.
    """
    template_name = 'detail_quote.html'

    def get_context_data(self, **kwargs):
        """
        Get a random quote, and put it in the context

        """
        context = super(QuoteView, self).get_context_data(**kwargs)
        if kwargs.has_key('quote'):
            quote = kwargs['quote']
        else:
            quote = get_object_or_404(Quote, pk=kwargs['id'])

        context['quote'] = quote
        context['url'] = reverse('detail', args=[quote.id,])

        """
        Get the meme, or the background
        """
        if quote.meme is not None:
            self.template_name = 'meme_quote.html'
            context['meme'] = quote.meme.image
        else:
            tags = quote.tags.all()
            # Background
            background = self.get_background(tags)
            context['background_image'] = background.url
        return context

    def get_background(self, tags=False):
        """
        Retrieve a random background

        :tags: list of tags
        """
        all_background_ids = BackgroundImage.objects.all().values('id')
        background_random_picker = CachedRandomPicker([item.get('id') for item in all_background_ids],'background_ids')

        # Background selection
        if len(tags) > 0:
            background_ids = BackgroundImage.objects.filter(tags__in=tags).values('id')
            background = background_random_picker.random_from_subset([item.get('id') for item in background_ids])
        else:
            background = background_random_picker.random()
        background = BackgroundImage.objects.get(pk=background)

        return background