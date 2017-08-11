from django.conf.urls import *

from . import views


urlpatterns = [
    url(r'(?P<mailbox>inbox|trash|sent)/$',
        view=views.message_list,
        name='messages'),

    url(r'compose(?:/(?P<content_type_id>\w+):(?P<object_id>\w+))?/$',
        view=views.message_create,
        name='create'),

    url(r'remove/(?P<object_id>\d+)/$',
        view=views.message_remove,
        name='remove'),

    url(r'(?P<object_id>\d+)/reply/$',
        view=views.message_reply,
        name='reply'),

    url(r'(?:(?P<mailbox>inbox|trash|sent)/)?(?P<object_id>\d+)/$',
        view=views.message_detail,
        name='message'),

    url(r'',
        view=views.message_list,
        name='messages'),
]
