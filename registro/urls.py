from django.conf.urls import include, url
from rest_framework import routers
from registro.views import CountryList, CountryViewSet

from registro.views import (
    CountryList,
    CountryCreation,
    CountryUpdate,
    CountryDelete
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'countries', CountryViewSet, base_name='countries_API')


urlpatterns = [

    url(r'^$', CountryList.as_view(), name='list'),
    url(r'^nuevo$', CountryCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', CountryUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', CountryDelete.as_view(), name='delete'),
    url(r'^API/', include(router.urls)),

]