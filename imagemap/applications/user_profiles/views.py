from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from applications.user_profiles.forms import UserProfileCreationForm
from applications.user_profiles.models import UserProfile


@login_required
def printable_card(request):
    data = dict()
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user__id=request.user.id)
        user_name = user_profile.user.username
        data["user_profile_form"] = UserProfileCreationForm(instance=user_profile)
        data["user_name"] = user_name

    return render_to_response('user_profiles/printable_card.html',
                              data,
                              context_instance=RequestContext(request))