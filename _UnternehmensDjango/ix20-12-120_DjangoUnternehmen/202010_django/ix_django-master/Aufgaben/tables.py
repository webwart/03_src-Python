from django_tables2 import Table, Column
from django.utils.html import format_html
from django.utils.timezone import datetime

from Aufgaben.models import Aufgabe


class AufgabeTable(Table):
    id = Column(visible=False)
    langtext = Column(visible=False)

    def render_kurztext(self, record, value):
        url = Aufgabe.objects.get(pk=record.id).get_absolute_url()
        html = format_html('<a href="{}">{}</a>', url, value)
        return html

    def render_vorlage_datum(self, record, value):
        today = datetime.now().date()
        value_date = value.strftime("%d.%m.%Y")
        if value < today:
            html = format_html('<span class="text-danger">{}</span>', value_date)
        else:
            html = value_date
        return html

    class Meta:
        model = Aufgabe
        per_page = 20
        order_by = ('vorlage_datum',)
        attrs = {"class": "table table-striped",
                 "thead": {
                     "class": "thead-light"
                    }
                 }
