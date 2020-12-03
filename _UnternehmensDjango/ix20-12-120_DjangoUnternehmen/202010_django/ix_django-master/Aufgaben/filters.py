from Aufgaben.models import Aufgabe
from django_filters import FilterSet, DateFilter
from bootstrap_datepicker_plus import DatePickerInput


class AufgabeFilter(FilterSet):
    vorlage_datum__gte = DateFilter(
        field_name='vorlage_datum',
        lookup_expr='gte',
        input_formats=["%d.%m.%Y"],
        label='Von Datum...',
        widget=DatePickerInput(
            options={"format": "DD.MM.YYYY",
                     "showClose": True,
                     "showClear": True,
                     "showTodayButton": True,
                     }
        ).start_of('vorlage'))

    vorlage_datum__lte = DateFilter(
        field_name='vorlage_datum',
        lookup_expr='lte',
        input_formats=["%d.%m.%Y"],
        label='...bis Datum',
        widget=DatePickerInput(
            options={"format": "DD.MM.YYYY",
                     "showClose": True,
                     "showClear": True,
                     "showTodayButton": True,
                     }
        ).end_of('vorlage'))

    class Meta:
        model = Aufgabe
        fields = {
            'kurztext': ['icontains', ],
            'status': ['exact', ],
            'liste': ['exact', ],
        }
