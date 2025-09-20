from django.db import models
from django.contrib import admin
class car(models.Model):
    number=models.IntegerField()
    mname=models.CharField(max_length=100)
    colour=models.CharField()
    year=models.IntegerField()
    price=models.IntegerField()

class carAdmin(admin.ModelAdmin):
    list_display=('number','mname','colour','year','price')

