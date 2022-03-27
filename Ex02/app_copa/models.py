from django.db import models
from django.utils import timezone

class Campeonato(models.Model):
    time1 = models.CharField(max_length=100, null=True, blank=True)
    time2 = models.CharField(max_length=20,  null=True, blank=True)
    local = models.CharField(max_length=100, null=True, blank=True)
    data = models.DateField(null=False, blank=False)
    hora = models.TimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    goltime1 = models.IntegerField(default=0, null=True, blank=True)
    goltime2 = models.IntegerField(default=0, null=True, blank=True)
    finalizado = models.BooleanField(default=False)
    class Meta:
        db_table = 'copa'
