from django.db import models
import socket

class Broker(models.Model):
    containers_count = models.IntegerField()
    current_region = models.CharField(max_length=10)
    container = models.ForeignKey('Container', on_delete=models.CASCADE, blank=True, null=True, default=None)

    def save(self, *args, **kwargs):
        for i in self.containers_count:
            print(self.containers_count)
            self.container.objects.create(port=9050 + i*2, cport=9051+i*2)
        super(Broker, self).save(*args, **kwargs)


class Container(models.Model):
    # name = models.CharField(blank=False, max_length=40)
    port = models.IntegerField(blank=False, unique=True)
    cport = models.IntegerField(blank=False, unique=True)
    is_busy = models.BooleanField(default=False)
    # broker = models.ForeignKey(Broker, on_delete=models.CASCADE)

    def run(self):
        pass

    def get_port(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0

    # def save(self, *args, **kwargs):
    #
    #     super(Container, self).save(*args, **kwargs)

class Region(models.Model):
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    region_index = models.CharField(max_length=2, blank=False)
    has_more = models.BooleanField(default=True)


class PortInUse(models.Model):
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    port = models.IntegerField()
