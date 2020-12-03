from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views.generic import CreateView, UpdateView

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


from Aufgaben.models import Aufgabe
from Aufgaben.tables import AufgabeTable
from Aufgaben.forms import AufgabeForm
from Aufgaben.filters import AufgabeFilter

from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from Aufgaben.serializers import AufgabeSerializer


class AufgabeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'Aufgaben.add_aufgabe'
    model = Aufgabe
    template_name = 'detail.html'
    form_class = AufgabeForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['TITLE_KURZ'] = 'Anlegen'
        context['TITLE_LANG'] = 'Aufgabe anlegen'
        return context


class AufgabeDetailView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'Aufgaben.change_aufgabe'
    model = Aufgabe
    template_name = 'detail.html'
    form_class = AufgabeForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['TITLE_KURZ'] = 'Bearbeiten'
        context['TITLE_LANG'] = 'Aufgabe bearbeiten'
        return context


class AufgabeFilterView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    template_name = 'liste.html'
    permission_required = 'Aufgaben.view_aufgabe'
    filterset_class = AufgabeFilter
    model = Aufgabe
    table_class = AufgabeTable


class MainView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    login_url = '/accounts/login/'
    permission_required = 'Aufgaben.view_aufgabe'
    filterset_class = AufgabeFilter
    template_name = 'aktuell.html'
    model = Aufgabe
    table_class = AufgabeTable


class AufgabeApiList(generics.ListCreateAPIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication,)
    permission_classes = (
        permissions.DjangoModelPermissions,
    )
    queryset = Aufgabe.objects.all()
    serializer_class = AufgabeSerializer
    ordering_fields = (
        'vorlage_datum',
    )


class AufgabeApiDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication,)
    permission_classes = (
        permissions.DjangoModelPermissions,
    )
    queryset = Aufgabe.objects.all()
    serializer_class = AufgabeSerializer
