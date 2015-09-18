from PIL import Image, ImageOps
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from utils.utils import Master
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import get_thumbnail

GENDER_CHOICES = (
    (0, _("male")),
    (1, _("female")),
    (2, _("gender_other")),
)


class DocumentType(Master):
    name = models.CharField(max_length=90, verbose_name=_('name'))
    abbr = models.CharField(max_length=10, verbose_name=_('abbr'))

    def __unicode__(self):
        return self.abbr

    class Meta:
        verbose_name = _('document_type')
        verbose_name_plural = _('document_types')


# function to return the correct UPLOAD_TO variable for the image field.
# All the images are storage in the folder with the name of the profile
def avatar_image_name(instance, filename):
    filename = filename.split('.')
    filename = str(instance.pk)+datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")+str('.')+str(filename[-1])
    return '/'.join(['img', 'avatars', slugify(instance.user.username), filename])


class UserProfile(Master):
    user = models.OneToOneField(User, related_name='profile', blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, upload_to=avatar_image_name, verbose_name=_("avatar"))
    about_me = models.TextField(max_length=220, blank=True, null=True, verbose_name=_("about_me"))
    document_id = models.IntegerField(null=True, blank=True, verbose_name=_("document_id"))
    document_type = models.ForeignKey(DocumentType, null=True, blank=True, verbose_name=_("document_type"))
    gender = models.SmallIntegerField(null=True, blank=True, choices=GENDER_CHOICES,
                                      verbose_name=_("gender"))
    telephone = models.IntegerField(null=True, blank=True, verbose_name=_("telephone"))
    cellphone = models.BigIntegerField(null=True, blank=True, verbose_name=_("cellphone"))
    address = models.TextField(null=True, blank=True, verbose_name=_("address"))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_("birth_date"))

    class Meta:
        verbose_name = _('user_profile')
        verbose_name_plural = _('user_profiles')

    def show_thumb(self, x, y):
        im = get_thumbnail(self.avatar, '%sx%s' % (x, y), crop='center', quality=99, format='JPEG')
        return im.url

    @property
    def hexagon_avatar(self):
        return self.show_thumb(150, 150)

    @property
    def get_full_name(self):
        return self.user.get_full_name()

    @property
    def get_short_name(self):
        return self.user.get_short_name()

    @property
    def email(self):
        return self.user.email

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    def __unicode__(self):
        return self.user.get_full_name()

    @property
    def gender_unicode(self):
        if self.gender is not None:
            return dict(GENDER_CHOICES)[self.gender].decode()