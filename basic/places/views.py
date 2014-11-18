from django.views.generic import DetailView, ListView
from basic.places.models import *


class CityDetail(DetailView):
    model = City


class CityList(ListView):
    model = City
    paginate_by = 20


class PlaceTypeDetail(DetailView):
    model = PlaceType


class PlaceTypeList(ListView):
    model = PlaceType
    paginate_by = 20


class PlaceDetail(DetailView):
    model = Place


class PlaceList(ListView):
    model = Place
    paginate_by = 20
