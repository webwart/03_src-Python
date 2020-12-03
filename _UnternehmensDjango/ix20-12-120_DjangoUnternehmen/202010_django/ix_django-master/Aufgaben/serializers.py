from rest_framework import serializers

from Aufgaben.models import Status, Liste, Aufgabe


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id',
                  'status_text',
                  )


class ListeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liste
        fields = ('id',
                  'liste_text',
                  )


class AufgabeSerializer(serializers.ModelSerializer):
    status = StatusSerializer(
        many=False,
        read_only=True,
    )
    liste = ListeSerializer(
        many=False,
        read_only=True,
    )

    class Meta:
        model = Aufgabe
        fields = ('id',
                  'kurztext',
                  'langtext',
                  'vorlage_datum',
                  'liste',
                  'status',
                  )
