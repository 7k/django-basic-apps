from django.conf.urls import *
from django_comments.urls import urlpatterns

from . import views


urlpatterns += [
    url(r'^(?P<object_id>\d+)/edit/$',
        view=views.comment_edit,
        name='comments-edit'),

    url(r'^(?P<object_id>\d+)/remove/$',
        view=views.comment_remove,
        name='comments-remove'),
]
