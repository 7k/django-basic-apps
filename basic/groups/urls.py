from django.conf.urls import *

from . import views


GROUP_URL = r'(?P<slug>[-\w]+)/'
PAGE_URL = r'%spages/(?P<page_slug>[-\w]+)/' % GROUP_URL
TOPIC_URL = r'%stopics/(?P<topic_id>\d+)/' % GROUP_URL
MESSAGE_URL = r'%smessages/(?P<message_id>\d+)/' % TOPIC_URL


urlpatterns = [
    url(r'^create/$',                           views.groups.group_create,         name='create'),
    url(r'^%s$' % GROUP_URL,                    views.groups.group_detail,         name='group'),
    url(r'^%sedit/$' % GROUP_URL,               views.groups.group_edit,           name='edit'),
    url(r'^%sremove/$' % GROUP_URL,             views.groups.group_remove,         name='remove'),
    url(r'^%sjoin/$' % GROUP_URL,               views.groups.group_join,           name='join'),
    url(r'^%smembers/$' % GROUP_URL,            views.groups.group_members,        name='members'),
    url(r'^%sinvite/$' % GROUP_URL,             views.groups.group_invite,         name='invite'),
    url(r'^$',                                  views.groups.group_list,           name='groups'),
]

# Topics
urlpatterns += [
    url(r'^%stopics/create/$' % GROUP_URL,      views.topics.topic_create,         name='topic_create'),
    url(r'^%s$' % TOPIC_URL,                    views.topics.topic_detail,         name='topic'),
    url(r'^%sedit/$' % TOPIC_URL,               views.topics.topic_edit,           name='topic_edit'),
    url(r'^%sremove/$' % TOPIC_URL,             views.topics.topic_remove,         name='topic_remove'),
    url(r'^%stopics/$' % GROUP_URL,             views.topics.topic_list,           name='topics'),
]

# Pages
urlpatterns += [
    url(r'^%spages/create/$' % GROUP_URL,       views.pages.page_create,          name='page_create'),
    url(r'^%s$' % PAGE_URL,                     views.pages.page_detail,          name='page'),
    url(r'^%sedit/$' % PAGE_URL,                views.pages.page_edit,            name='page_edit'),
    url(r'^%sremove/$' % PAGE_URL,              views.pages.page_remove,          name='page_remove'),
    url(r'^%spages/$' % GROUP_URL,              views.pages.page_list,            name='pages'),
]

# Messages
urlpatterns += [
    url(r'^%smessages/create/$' % TOPIC_URL,    views.messages.message_create,       name='message_create'),
    url(r'^%s$' % MESSAGE_URL,                  views.messages.message_detail,       name='message'),
    url(r'^%sedit/$' % MESSAGE_URL,             views.messages.message_edit,         name='message_edit'),
    url(r'^%sremove/$' % MESSAGE_URL,           views.messages.message_remove,       name='message_remove'),
    url(r'^%smessages/$' % TOPIC_URL,           views.messages.message_list,         name='messages'),
]
