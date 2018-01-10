from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Country
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from .serializers import CountrySerializer
from django.views.generic import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from rest_framework import viewsets



class CountryList(ListView):
    model = Country

class CountryCreation(CreateView):
    model = Country
    success_url = reverse_lazy('countries:list')
    fields = ['name', 'code']


class CountryUpdate(UpdateView):
    model = Country
    success_url = reverse_lazy('countries:list')
    fields = ['name', 'code']


class CountryDelete(DeleteView):
    model = Country
    success_url = reverse_lazy('countries:list')


class CountryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CountrySerializer
    queryset = Country.objects.all()