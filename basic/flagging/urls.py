from django.conf.urls import *

from . import views


urlpatterns = [
    url(r'^flag/(?P<slug>[-\w]+)/(?P<app_label>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/$',
        view=views.flag,
        name='flag'
    ),
    url(r'^unflag/(?P<slug>[-\w]+)/(?P<app_label>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/$',
        view=views.unflag,
        name='unflag'
    ),
    url(r'^(?P<username>[-\w]+)/(?P<slug>[-\w]+)/$',
        view=views.user_flags,
        name='user_flags'
    ),
]