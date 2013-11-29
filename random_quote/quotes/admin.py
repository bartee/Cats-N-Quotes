__author__ = 'bartstroeken'

from django.contrib import admin
from quotes.models import Quote, BackgroundImage, Tag, Meme

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'comeback','quote_tags','author','avatar_admin_html']
    list_filter = ['author', 'original_author']

    def quote_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])
    quote_tags.short_description = "Tags"


class BackgroundImageAdmin(admin.ModelAdmin):

    list_display = ['background_thumb', 'background_tags']

    def background_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])
    background_tags.short_description = "Tags"

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Meme)
admin.site.register(BackgroundImage, BackgroundImageAdmin)
admin.site.register(Tag, TagAdmin)
