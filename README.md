# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'manufacturer', 'model_name', 'year', 'price')
    list_filter = ('year', 'manufacturer')
    search_fields = ('model_name', 'manufacturer')

admin.site.register(Car, CarAdmin)

models.py

from django.db import models

class Car(models.Model):
    car_id = models.IntegerField()
    model_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.FloatField()

    def str(self):
        return f"{self.manufacturer} {self.model_name} ({self.year})"


## OUTPUT
![alt text](<Screenshot (4).png>)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
