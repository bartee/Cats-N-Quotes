__author__ = 'bartstroeken'
from django.db.models import Manager
from django.core.cache import *
from random import choice, randint


class CachedRandomPicker(object):

    def __init__(self, items, cache_key, cache_fraction=0.1):
        """
        Pick a random number from a list of values.
        Cache the last items, and exclude them from the list, to improve randomness.

        items: the list of items to handle
        cache_key: the cache key to be used
        cache_fraction: the items size fraction to be stored in cache. Increasing this number (between 0 and 1) will improve randomness


        """
        self.cache_key = cache_key
        self.items = items
        self.cache_fraction = cache_fraction

    def get_from_cache(self):
        """
        Get the cached value from the cache
        """
        self.cached_values = cache.get(self.cache_key)
        if not self.cached_values:
            self.cached_values = []
        self.cache_length = int(len(self.items) * self.cache_fraction)

    def store_in_cache(self, value):
        """
        pop the first item off the cached_values if necessary, and append the new one to the end

        :param value: item to be stored in the cache.
        """
        if len(self.cache_values) > self.cache_length:
            self.cached_values.pop(0)
        self.cached_values.append(value)
        # Store that value in the cache
        cache.set(self.cache_key, self.cached_values)

    def random(self):
        """
        Get a random value from a list
        """
        self.get_from_cache()

        target_set = list(set(self.items).difference(set(self.cached_values)))
        # Make a choice
        value = choice(target_set)
        self.store_in_cache(value)

        # Finally, return the value
        return value

    def random_from_subset(self,subset):
        """
        Sometimes, you want to use the same cached values, but select from a different subset.
        That's why this is here.
        First, diff the subset with the cached_values. If there's still some items left, select from that
        Otherwise, fall back to the normal way of selecting from all items

        subset: a list of items to be diffed
        """
        self.get_from_cache()
        sample = list(set(subset).difference(set(self.cached_values)))
        if len(sample) > 0:
            value = choice(sample)
            self.store_in_cache(value)
            return value
        return self.random()
