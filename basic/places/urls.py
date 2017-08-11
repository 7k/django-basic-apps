from django.conf.urls import *

from .views import CityDetail, CityList
from .views import PlaceTypeDetail, PlaceTypeList
from .views import PlaceDetail, PlaceList

urlpatterns = [
    url(r'^cities/(?P<slug>[-\w]+)/$',
        view=CityDetail.as_view(),
        name='place_city_detail'
    ),
    url(r'^cities/$',
        view=CityList.as_view(),
        name='place_city_list'
    ),
    url(r'^types/(?P<slug>[-\w]+)/$',
        view=PlaceTypeDetail.as_view(),
        name='place_type_detail'
    ),
    url(r'^types/$',
        view=PlaceTypeList.as_view(),
        name='place_type_list'
    ),
    url(r'^(?P<slug>[-\w]+)/$',
        view=PlaceDetail.as_view(),
        name='place_detail'
    ),
    url(r'^$',
        view=PlaceList.as_view(),
        name='place_list'
    ),
]
