from django.db import models
from django.core.validators import MinValueValidator ,MaxValueValidator

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])

    def __str__(self):
        return f"{self.first_name},{self.last_name} is {self.age} years or old"

class Review(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    age = models.IntegerField()