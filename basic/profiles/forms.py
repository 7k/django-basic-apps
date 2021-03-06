from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from basic.profiles.models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ()


ServiceFormSet  = inlineformset_factory(Profile, Service, exclude=[])
LinkFormSet     = inlineformset_factory(Profile, Link, exclude=[])


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
