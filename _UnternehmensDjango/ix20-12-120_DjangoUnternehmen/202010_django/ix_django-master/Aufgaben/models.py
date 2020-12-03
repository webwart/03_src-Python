from django.db import models
from django.urls import reverse

# Create your models here.

class Status(models.Model):
    status_text = models.CharField(max_length=20)

    def __str__(self):
        return self.status_text


class Liste(models.Model):
    liste_text = models.CharField(max_length=30)

    def __str__(self):
        return self.liste_text


class Aufgabe(models.Model):
    kurztext = models.CharField(max_length=100)
    langtext = models.TextField(blank=True)
    vorlage_datum = models.DateField(verbose_name='Vorlage')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    liste = models.ForeignKey(Liste, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.kurztext

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk })