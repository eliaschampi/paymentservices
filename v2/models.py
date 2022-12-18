from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    logo = models.CharField(max_length=100)