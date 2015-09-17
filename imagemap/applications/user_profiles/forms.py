from random import randint
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from applications.user_profiles.models import UserProfile


class AuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label=_("remember_me"))


class UserProfileCreationForm(forms.ModelForm):
    """
    A form that creates a user profile, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'username_exist': _("The user exist."),
        'username_has_whitespaces': _("The username can't contain whitespaces."),
    }
    #username = forms.CharField(label=_("Username"))
    email = forms.EmailField(label=_("email"))
    first_names = forms.CharField(label=_("first_names"))
    last_names = forms.CharField(label=_("last_names"))
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))
    conditions = forms.BooleanField(label="", required=True, help_text=_("i have read the terms and conditions"))

    class Meta:
        model = UserProfile
        fields = ["first_names", "last_names", "password1", "password2", "email", "conditions"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user_profile = super(UserProfileCreationForm, self).save(commit=False)
        rand_username = randint(10000000, 999999999)
        while User.objects.filter(username=rand_username).exists():
            rand_username = randint(10000000, 999999999)
        username = rand_username
        password = self.cleaned_data["password1"]
        email = self.cleaned_data["email"]
        first_names = self.cleaned_data.get("first_names")
        last_names = self.cleaned_data.get("last_names")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                self.error_messages['username_exist'],
                code='username_exist',
            )
        else:
            user = User(username=username, email=email)
            user.set_password(password)

        user.first_name = first_names
        user.last_name = last_names
        if commit:
            user_profile.save()
            user.save()
            user_profile.user = user
            user_profile.save()
        user_profile = super(UserProfileCreationForm, self).save()
        return user_profile