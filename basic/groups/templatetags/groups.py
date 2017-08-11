from django import template
from django.db import models

from basic.groups.models import GroupMember

register = template.Library()


@register.filter
def is_member(group, user):
    return GroupMember.objects.is_member(group, user)


@register.filter
def is_owner(group, user):
    return GroupMember.objects.is_owner(group, user)


@register.filter
def is_moderator(group, user):
    return GroupMember.objects.is_moderator(group, user)