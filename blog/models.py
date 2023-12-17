from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    salary = models.FloatField()
    
    def __str__(self):
        return self.name