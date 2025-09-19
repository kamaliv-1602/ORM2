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
