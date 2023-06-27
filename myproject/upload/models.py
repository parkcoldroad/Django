from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class Documentation(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')