from django import forms
from applications.images.models import UploadedImages


class AddMarkForm(forms.ModelForm):
    form_name = forms.CharField(initial='map_form', widget=forms.HiddenInput)

    class Meta:
        model = UploadedImages
        fields = ['image', 'position']