from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # Examples:
     url(r'^$', views.home, name='home'),
     url(r'^fields/$', views.FieldListView.as_view(), name='field-list'),
     url(r'^(?P<facet_field>[a-zA-Z0-9_\w \.]+)/facets/$', views.FieldFacetListView.as_view(), name='facet-list'),
    # url(r'^blog/', include('blog.urls')),

)
