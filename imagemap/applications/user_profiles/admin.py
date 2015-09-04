from django.contrib import admin
from applications.user_profiles.models import UserProfile, DocumentType

admin.site.register(UserProfile)
admin.site.register(DocumentType)
