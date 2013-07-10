__author__ = 'bartstroeken'

from django.contrib import admin
from quotes.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'comeback','author','avatar_html']
    list_filter = ['author', 'original_author']
    # list_editable = ['comeback', 'author']

admin.site.register(Quote, QuoteAdmin)
