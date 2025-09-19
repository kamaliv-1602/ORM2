# Ex02 Django ORM Web Application
## Date: 19.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
~~~
models.py
from django.db import models

# Create your models here.
from django.contrib import admin

class Car(models.Model):
    name = models.CharField(max_length=255, help_text="Car Name")
    brand = models.CharField(max_length=100, help_text="Car Brand")
    model_year = models.IntegerField(help_text="Manufacturing Year")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Car Price")
    fuel_type = models.CharField(max_length=50, help_text="Fuel Type (Petrol/Diesel/Electric)")
    seating_capacity = models.IntegerField(help_text="Seating Capacity")
    
class CarAdmin(admin.ModelAdmin):
    list_display=('name','brand','model_year','price','fuel_type','seating_capacity')

admin.py
from django.contrib import admin

# Register your models here.
from.models import Car,CarAdmin
admin.site.register(Car,CarAdmin)
~~~

## OUTPUT
![alt text](<Screenshot 2025-09-16 152351.png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
