__author__ = 'bartstroeken'

from django.contrib import admin
from models import Quote, BackgroundImage, Meme

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'comeback','author','avatar_html']
    list_filter = ['author', 'original_author']
    # list_editable = ['comeback', 'author']
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['background_thumb']
    # list_editable = ['comeback', 'author']

admin.site.register(Quote, QuoteAdmin, Meme)
admin.site.register(BackgroundImage, BackgroundImageAdmin)
