from django.contrib import admin
from applications.images.models import UploadedImages, Images


admin.site.register(UploadedImages)
admin.site.register(Images)
