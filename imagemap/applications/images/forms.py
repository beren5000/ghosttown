from django import forms
from applications.images.models import UploadedImages


class AddMarkForm(forms.ModelForm):
    class Meta:
        model = UploadedImages
        fields = ['image', 'position']