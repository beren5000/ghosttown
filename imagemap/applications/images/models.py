from datetime import datetime
from django.db import models
from utils.utils import Master
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import get_thumbnail
from django.utils.text import slugify
from geoposition.fields import GeopositionField


# function to return the correct UPLOAD_TO variable for the image field.
# All the images are storage in the folder with the name of the book
def image_name(instance, filename):
    filename = filename.split('.')
    filename = str(instance.id)+"at"+datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")+str('.')+str(filename[-1])
    return '/'.join(['img', 'uploaded', slugify(instance.user_profile.id), filename])


class UploadedImages(Master):
    user_profile = models.ForeignKey('user_profiles.UserProfile', verbose_name=_("user_profile"))
    image = models.ImageField(blank=True, null=True, upload_to=image_name, verbose_name=_("image"))
    position = GeopositionField(verbose_name=_('map_position'))

    class Meta:
        verbose_name = _("uploaded_image")
        verbose_name_plural = _("uploaded_images")


class Images(Master):
    image = models.ImageField(blank=True, null=True, upload_to=image_name, verbose_name=_("image"))
    caption = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("caption"))

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")