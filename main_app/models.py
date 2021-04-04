from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Ramen(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=6)
    description = models.TextField(max_length=380)
    rating = models.IntegerField()

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"ramen_id": self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    ramen = models.ForeignKey(Ramen, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for ramen_id: {self.ramen_id} @{self.url}"