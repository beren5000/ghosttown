# -*- coding: utf-8 -*-
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from applications.images.forms import AddMarkForm
from applications.images.models import Images, UploadedImages
from applications.user_profiles.forms import UserProfileCreationForm, AuthenticationForm
from applications.user_profiles.models import UserProfile


def logout_view(request):
    print 'im here'
    logout(request)
    print request.user.is_authenticated()
    return HttpResponseRedirect(reverse('index'))


def index_view(request):
    data = dict()
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user__id=request.user.id)
        user_name = user_profile.user.username
        data["user_profile_form"] = UserProfileCreationForm(instance=user_profile)
        data["user_name"] = user_name
    else:
        data["login_form"] = AuthenticationForm()
        data["user_profile_form"] = UserProfileCreationForm()
        data["user_name"] = 'X X X X X X X X'

    if request.method == 'POST':
        form_name = request.POST.get('form_name')
        #change and actualize both forms
        if form_name == 'register_form':
            user_profile_form = UserProfileCreationForm(request.POST, request.FILES)
            if user_profile_form.is_valid():
                user_profile_form.save()
                username = user_profile_form.instance.user.username
                password = request.POST.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                user_profile_form = UserProfileCreationForm(instance=user_profile_form.instance)
            data["user_profile_form"] = user_profile_form
        elif form_name == 'login_form':
            print request.POST
            login_form = AuthenticationForm(data=request.POST)
            print login_form
            print login_form.is_valid()
            if login_form.is_valid():
                if not login_form.cleaned_data['remember_me']:
                    request.session.set_expiry(0)
                login(request, login_form.get_user())
                print request.user
                return HttpResponseRedirect(reverse('index'))
            data["login_form"] = login_form

    data["gallery"] = Images.objects.filter(is_active=True)
    data["marks"] = UploadedImages.objects.filter(is_active=True)
    data["user_profiles"] = UserProfile.objects.filter(is_active=True)

    return render_to_response('images/index.html',
                              data,
                              context_instance=RequestContext(request))

@login_required
def image_map_view(request):
    data = dict()
    user_profile = UserProfile.objects.get(user__id=request.user.id)
    try:
        mark = UploadedImages.objects.latest('created')
        map_form = AddMarkForm(instance=mark)
    except UploadedImages.DoesNotExist:
        map_form = AddMarkForm()

    if request.method == 'POST':
        map_form = AddMarkForm(request.POST, request.FILES)
        if map_form.is_valid():
            mark = map_form.save()
            mark.user_profile = user_profile
            mark.save()
            map_form = AddMarkForm(instance=mark)

    data["map_form"] = map_form
    return render_to_response('images/addImage.html',
                              data,
                              context_instance=RequestContext(request))