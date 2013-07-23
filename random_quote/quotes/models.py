from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quote(models.Model):
    quote = models.CharField(max_length=255,help_text='De Quote')
    comeback = models.CharField(max_length=255,blank=True, help_text='Wanneer er een nifty comeback is, voeg hem toe')
    original_author = models.CharField(max_length=100, help_text='wie heeft hem in het leven geroepen? Vul zijn/haar email adres in om een Gravatar op te halen', blank=True)
    author = models.ForeignKey(User,verbose_name='User')
    pub_date = models.DateTimeField('date published',auto_now_add=True,editable=False)

    def __unicode__(self):
        return self.quote

    @property
    def avatar(self):
        """
        The avatar is auto-generated from the original_author-field. That's hashed, and sent to www.gravatar.com
        """
        admin_user = User.objects.get(pk=1)
        email = self.original_author

        if self.author != admin_user:
            email = self.author.email
        import hashlib
        value = hashlib.md5(email)
        return 'http://www.gravatar.com/avatar/%s' % value.hexdigest() + '?s=200'

    @property
    def authorname(self):
        admin_user = User.objects.get(pk=1)
        user= self.original_author.split('@')
        username = user[0]

        if self.author != admin_user:
            username = self.author.first_name + ' ' + self.author.last_name
        return username


    def avatar_html(self):
        admin_user = User.objects.get(pk=1)
        if self.author != admin_user:
            return u'<img src="%s" title="%s" width="160"/>' % (self.avatar, self.author.first_name+" "+self.author.last_name)
        return u'<img src="%s" />' % self.avatar

    avatar_html.allow_tags = True


