from django.db import models
import os

# Create your models here.
class Broker(models.Model):
    max_containers = models.IntegerField()

    free_ports = models.Choices()
    free_cports = models.Choices()

class Container(models.Model):
    name = models.CharField(blank=False, max_length=40)
    port = models.IntegerField(blank=False, default=9050, unique=True)
    cport = models.IntegerField(blank=False, default=9051, unique=True)
    is_busy = models.BooleanField(default=False)

    def run(self):
        pass

    def stop(self):
        pass


