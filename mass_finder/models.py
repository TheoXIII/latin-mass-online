from django.db import models

class Churches(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    low_mass = models.BooleanField(default = False)
    sung_mass = models.BooleanField(default = False)
    high_mass = models.BooleanField(default = False)
    address = models.CharField(max_length=255, default="")
    image_url = models.CharField(max_length=255, default="")
    website = models.CharField(max_length=255, default="")
    gmap = models.TextField(default="")
    mass_times = models.TextField(default="")
