from datetime import datetime
from random import randint
from django.db import models
from django.utils import importlib
from utils.utils import Master
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import get_thumbnail
from django.utils.text import slugify
from geoposition.fields import GeopositionField

try:
    from rol import settings_name
except ImportError:
    settings_name = "settings"

settings_var = "imagemap."+settings_name
settings = importlib.import_module(settings_var)

# function to return the correct UPLOAD_TO variable for the image field.
# All the images are storage in the folder with the name of the book
def image_name(instance, filename):
    filename = filename.split('.')
    filename = str(instance.id)+"at"+datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")+str('.')+str(filename[-1])
    return '/'.join(['img', 'uploaded', slugify(instance.id), filename])


class UploadedImages(Master):
    user_profile = models.ForeignKey('user_profiles.UserProfile', blank=True, null=True, verbose_name=_("user_profile"))
    image = models.ImageField(blank=True, null=True, upload_to=image_name, verbose_name=_("image"))
    position = GeopositionField(verbose_name=_('map_position'))

    class Meta:
        verbose_name = _("uploaded_image")
        verbose_name_plural = _("uploaded_images")

    def show_thumb(self, x, y):
        im = get_thumbnail(self.image, '%sx%s' % (x, y), crop='center', quality=99, format='JPEG')
        return im.url

    @property
    def thumb_map(self):
        if self.image:
            return self.show_thumb(160, 160)
        rand = str(randint(1, 4))
        return settings.STATIC_URL+"ghosttown/img/Seccion4-IconExample-"+rand+".svg"


# function to return the correct UPLOAD_TO variable for the image field.
# All the images are storage in the folder with the name of the book
def image_name_images(instance, filename):
    filename = filename.split('.')
    filename = str(instance.id)+"at"+datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")+str('.')+str(filename[-1])
    return '/'.join(['img', 'statics', filename])


class Images(Master):
    image = models.ImageField(blank=True, null=True, upload_to=image_name_images, verbose_name=_("image"))
    caption = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("caption"))

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def show_thumb(self, x, y):
        im = get_thumbnail(self.image, '%sx%s' % (x, y), crop='center', quality=99, format='JPEG')
        return im.url

    @property
    def thumb_home(self):
        return self.show_thumb(160, 160)

