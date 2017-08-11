from django.conf.urls import *
from django.views.generic.simple import direct_to_template

from . import views


urlpatterns = [
    url(r'^genres/(?P<slug>[-\w]+)/$',
        view=views.genre_detail,
        name='music_genre_detail',
    ),
    url (r'^genres/$',
        view=views.genre_list,
        name='music_genre_list',
    ),
    url(r'^labels/(?P<slug>[-\w]+)/$',
        view=views.label_detail,
        name='music_label_detail',
    ),
    url (r'^labels/$',
        view=views.label_list,
        name='music_label_list',
    ),
    url(r'^bands/(?P<slug>[-\w]+)/$',
        view=views.band_detail,
        name='music_band_detail',
    ),
    url (r'^bands/$',
        view=views.band_list,
        name='music_band_list',
    ),
    url(r'^albums/(?P<slug>[-\w]+)/$',
        view=views.album_detail,
        name='music_album_detail',
    ),
    url (r'^albums/$',
        view=views.album_list,
        name='music_album_list',
    ),
    url(r'^tracks/(?P<slug>[-\w]+)/$',
        view=views.track_detail,
        name='music_track_detail',
    ),
    url (r'^tracks/$',
        view=views.track_list,
        name='music_track_list',
    ),
]


urlpatterns += [
    url (r'^$',
        view=direct_to_template,
        kwargs={'template': 'music/index.html'},
        name='music_index',
    ),
]