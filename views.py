from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from solrinspector import api as solr_api
from getenv import env

SOLR_URL = env("SOLR_URL", "http://localhost:8983/solr/")



# Create your views here.
def home(request):
    """docstring for home"""
    field_list = ','.join( [ f.name for f in solr_api.list_fields(SOLR_URL)])
    return HttpResponse("Solr Url: %s" % field_list)


class FieldListView(ListView):
    template_name = "inspectsolr/field_list.html"

    def get_queryset(self):
        return solr_api.list_fields(SOLR_URL)

class FieldFacetListView(ListView):
    template_name = "inspectsolr/facet_list.html"

    def get_queryset(self):
        return solr_api.get_facets(SOLR_URL, self.kwargs['facet_field'])
