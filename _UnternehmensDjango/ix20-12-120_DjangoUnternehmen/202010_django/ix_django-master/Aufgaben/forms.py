from django.forms import ModelForm, DateField
from Aufgaben.models import Aufgabe
from bootstrap_datepicker_plus import DatePickerInput


class AufgabeForm(ModelForm):
    vorlage_datum = DateField(input_formats=["%d.%m.%Y"], label="Vorlage",
                              widget=DatePickerInput(
                                  options={
                                      "format": "DD.MM.YYYY",
                                      "showClose": True,
                                      "showClear": True,
                                      "showTodayButton": True,
                                  }
                              ))

    class Meta:
        model = Aufgabe
        fields = (
            'id',
            'kurztext',
            'langtext',
            'vorlage_datum',
            'status',
            'liste',
        )

