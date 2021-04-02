from django.db import models

# Create your models here.
class Ramen(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=6)
    description = models.TextField(max_length=380)
    rating = models.IntegerField()

    def __str__(self):
        return self.name 
        