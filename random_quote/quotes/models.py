from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.CharField(max_length=255,help_text='De Quote')
    comeback = models.CharField(max_length=255,blank=True, help_text='Wanneer er een nifty comeback is, voeg hem toe')
    original_author = models.CharField(max_length=100, help_text='wie heeft hem in het leven geroepen?')
    pub_date = models.DateTimeField('date published',auto_now_add=True,editable=False)

    def __unicode__(self):
        return self.quote

    @property
    def avatar(self):
        """
        The avatar is auto-generated from the original_author-field. That's hashed, and sent to www.gravatar.com
        """
        import hashlib
        value = hashlib.md5(self.original_author)
        return 'http://www.gravatar.com/avatar/%s' % value.hexdigest()


    def avatar_html(self):
        return u'<img src="%s" />' % self.avatar

    avatar_html.allow_tags = True


