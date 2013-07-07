__author__ = 'bartstroeken'

from django.contrib import admin
from quotes.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'comeback','avatar_html']

admin.site.register(Quote, QuoteAdmin)
