from django.urls import path
from django.conf.urls import url

from .views import MainView, AufgabeCreateView, AufgabeDetailView, AufgabeFilterView, \
    AufgabeApiList, AufgabeApiDetail

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('aufgabe/anlegen/', AufgabeCreateView.as_view(), name='anlegen'),
    path('aufgabe/<int:pk>/', AufgabeDetailView.as_view(), name='detail'),
    url(r'^aufgabe/liste/$', AufgabeFilterView.as_view(), name='liste'),

    url(r'^aufgabe/api/$', AufgabeApiList.as_view(), name='api_list'),
    url(r'^aufgabe/api/(?P<pk>[0-9]+)$', AufgabeApiDetail.as_view(), name='api_detail'),
]
