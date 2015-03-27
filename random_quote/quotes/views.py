__author__ = 'Andrew Gerssen'

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.conf import settings
from os import listdir
from random import choice

from django.contrib.auth.models import User
from quotes.util import CachedRandomPicker
from models import Quote, BackgroundImage

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

        random_cat_template = 'little_spinner'

        dir = settings.PROJECT_ROOT +'/quotes/templates/cats/'
        templates = listdir(dir)
        context['random_cat_template'] = 'cats/' + choice(templates)

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

class AuthorView(QuoteView):
    """
    Get a random quote of an author

    First, see if you can get the author by login. If so, return that author. If not, redirect to home.

    """

    def dispatch(self, request, *args, **kwargs):
        """
        Get a random quote for a certain user, and put it in the context.
        The application will redirect to home when:
         - the user cannot be found
         - the user has no IDs


        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        author_name = kwargs.get('author_name')

        try:
            author = User.objects.get(username=author_name)
        except ObjectDoesNotExist, e:
            # Author cannot be found, redirect to home
            return HttpResponseRedirect(reverse('home'))

        quote_ids = Quote.objects.filter(author=author).all().values('id')
        if len(quote_ids) == 0:
            # No more quotes have been found, redirect to home
            return HttpResponseRedirect(reverse('home'))

        cache_key = 'random_quotes_%s'.format(author_name.lower())
        quote_random_picker = CachedRandomPicker([item.get('id') for item in quote_ids], cache_key, 0.2, 0)
        self.quote = Quote.objects.get(pk=quote_random_picker.random())

        return super(AuthorView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """


        """
        kwargs = {'quote':self.quote}

        return super(AuthorView, self).get_context_data(**kwargs)
