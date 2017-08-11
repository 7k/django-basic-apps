from django.conf.urls import *

from .views import ProfileDetail, ProfileList, profile_edit

USERNAME = r'(?P<username>[-.\w]+)'

urlpatterns = [
    url(r'^edit/$',
        view=profile_edit,
        name='profile_edit',
    ),
    url(r'^%s/$' % USERNAME,
        view=ProfileDetail.as_view(),
        name='profile_detail',
    ),
    url (r'^$',
        view=ProfileList.as_view(),
        name='profile_list',
    ),
]
