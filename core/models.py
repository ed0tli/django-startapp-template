from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class CustomUser(AbstractUser):
    phone = models.CharField(_(u"Phone"), max_length=32, blank=True, null=True)
    tagline = models.CharField(max_length=140, blank=True)
    avatar = models.ImageField(_('Avatar'), upload_to ='upload/avatar', blank=True)

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return u' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return u'%s' % self.first_name

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return settings.DEFAULT_AVATAR
