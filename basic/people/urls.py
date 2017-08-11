from django.conf.urls import *

from . import views


urlpatterns = [
    url(r'^types/(?P<slug>[-\w]+)/$',
        view=views.person_type_detail,
        name='person_type_detail'
    ),
    url (r'^types/$',
        view=views.person_type_list,
        name='person_type_list'
    ),
    url(r'^(?P<slug>[-\w]+)/$',
        view=views.person_detail,
        name='person_detail'
    ),
    url (r'^$',
        view=views.person_list,
        name='person_list'
    ),
    url(r'^quotes/(?P<slug>[-\w]+)/$',
        view=views.person_quote_list,
        name='person_quote_list'
    ),
    url(r'^quote/(?P<quote_id>\d+)/$',
        view=views.quote_detail,
        name='quote_detail'
    ),
]
