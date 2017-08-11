from django.conf.urls import *

from . import views


USERNAME = r'(?P<username>[-.\w]+)'

urlpatterns = [
    url(r'^following/%s/$' % USERNAME,
        view=views.following,
        name='relationship_following'
    ),
    url(r'^followers/%s/$' % USERNAME,
        view=views.followers,
        name='relationship_followers'
    ),
    url(r'^follow/%s/$' % USERNAME,
        view=views.follow,
        name='relationship_follow'
    ),
    url(r'^unfollow/%s/$' % USERNAME,
        view=views.unfollow,
        name='relationship_unfollow'
    ),
    url(r'^block/%s/$' % USERNAME,
        view=views.block,
        name='relationship_block'
    ),
    url(r'^unblock/%s/$' % USERNAME,
        view=views.unblock,
        name='relationship_unblock'
    ),
]
