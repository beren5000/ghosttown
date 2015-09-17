import random
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from applications.user_profiles.forms import UserProfileCreationForm
from applications.user_profiles.models import UserProfile


def index_view(request):
    data = dict()
    data["user_profile_form"] = UserProfileCreationForm()

    if request.user.is_authenticated():
        user_name = UserProfile.objects.get(user__id=request.user.id).get_full_name
        data["user_name"] = user_name

    if request.method == 'POST':
        user_profile_form = UserProfileCreationForm(request.POST)
        if user_profile_form.is_valid():
            user_profile_form.save()
            data["user_profile_form"] = user_profile_form
    return render_to_response('images/index.html',
                              data,
                              context_instance=RequestContext(request))