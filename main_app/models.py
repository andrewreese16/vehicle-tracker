from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Vehicle(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vehicles")
  make = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  year = models.IntegerField()
  vin = models.CharField(max_length=17, unique=True)

  def __str__(self):
    return f"{self.year} {self.make} {self.model}"
  

class MaintenanceWork(models.Model):
  vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenance_records')
  name = models.CharField(max_length=100)
  miles_at_work= models.IntegerField()
  product_link = models.URLField(blank=True, null=True)
  part_number = models.CharField(max_length=50, blank=True, null=True)
  price_of_work = models.IntegerField()
  notes = models.TextField(blank=True, null=True)
  date_added = models.DateTimeField(auto_now_add=True)
  date_of_service = models.DateField(default=date.today)

  def __str__(self):
    return f"{self.name} at {self.miles_at_work} miles"