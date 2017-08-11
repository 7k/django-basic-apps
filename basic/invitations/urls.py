from django.conf.urls import *

from . import views


urlpatterns = [
    url(r'^send/$',
        view=views.invitation_create,
        name='create'),

    url(r'^(?P<token>\w+)/$',
        view=views.invitation_detail,
        name='invitation'),
]