from django.db import models

class Phone(models.Model):
    brand = models.CharField(max_length= 50)
    model = models.CharField(max_length=50)
    storage = models.CharField(max_length= 20)
    color = models.CharField(max_length=50)
    release_date = models.IntegerField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__ (self):
        return self.brand


