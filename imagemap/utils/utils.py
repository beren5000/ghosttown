from django.db import models
from django.utils.translation import ugettext_lazy as _
from audit_log.models import AuthStampedModel


class Master(AuthStampedModel):

    description = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('description'))
    is_active = models.BooleanField(default=True, verbose_name=_("is_active"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    modified = models.DateTimeField(auto_now=True, verbose_name=_("modified"))

    class Meta:
        abstract = True