from django.db import models

# Create your models here.

class Organization(models.Model):
    yearcode = models.IntegerField(blank=True, null=True)
    periodcode = models.IntegerField(blank=True, null=True)
    inn = models.CharField(max_length=1000, blank=True, null=True)
    ogrn = models.CharField(max_length=1000, blank=True, null=True)
    regionname = models.CharField(max_length=1000, blank=True, null=True)
    namep = models.CharField(max_length=1000, blank=True, null=True)
    namec = models.CharField(max_length=1000, blank=True, null=True)
    invalid = models.BooleanField(blank=True, null=True)
    okved2 = models.CharField(max_length=1000, blank=True, null=True)
    okved2name = models.CharField(max_length=1000, blank=True, null=True)
    token = models.CharField(max_length=1000, blank=True, null=True)
    kpprafp = models.CharField(max_length=1000, blank=True, null=True)
    is_protch_przd = models.BooleanField(blank=True, null=True)
    foreignorg = models.BooleanField(blank=True, null=True)
    okopf12 = models.CharField(max_length=1000, blank=True, null=True)
    pr_otch = models.CharField(max_length=1000, blank=True, null=True)
    pr_otch_zd_date = models.CharField(max_length=1000, blank=True, null=True)
    pr_rafp = models.CharField(max_length=1000, blank=True, null=True)
    pr_zd = models.CharField(max_length=1000, blank=True, null=True)
    rsmpcategory = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    date_vyp = models.CharField(max_length=1000, blank=True, null=True)
    date_entry = models.CharField(max_length=1000, blank=True, null=True)
    date_ogrn = models.CharField(max_length=1000, blank=True, null=True)
    date_post = models.CharField(max_length=1000, blank=True, null=True)
    date_reg = models.CharField(max_length=1000, blank=True, null=True)
    build = models.CharField(max_length=1000, blank=True, null=True)
    post_index = models.CharField(max_length=1000, blank=True, null=True)
    kpp = models.CharField(max_length=1000, blank=True, null=True)
    kod_no = models.CharField(max_length=1000, blank=True, null=True)
    kod_okved = models.CharField(max_length=1000, blank=True, null=True)
    kod_ro = models.CharField(max_length=1000, blank=True, null=True)
    kod_region = models.CharField(max_length=1000, blank=True, null=True)
    corpus = models.CharField(max_length=1000, blank=True, null=True)
    tax_dept_name = models.CharField(max_length=1000, blank=True, null=True)
    main_okved_name = models.CharField(max_length=1000, blank=True, null=True)
    tax_dept_name_main = models.CharField(max_length=1000, blank=True, null=True)
    ul_reg_method = models.CharField(max_length=1000, blank=True, null=True)
    ul_street = models.CharField(max_length=1000, blank=True, null=True)
    ogrn = models.CharField(max_length=1000, blank=True, null=True)
    region_type = models.CharField(max_length=1000, blank=True, null=True)
    street_type = models.CharField(max_length=1000, blank=True, null=True)
    other_data = models.JSONField(blank=True, default=None, null=True)


    def __str__(self):
        return self.namec

import os
import socket

class Broker(models.Model):
    containers_count = models.IntegerField()
    current_region = models.CharField(max_length=10)


class Container(models.Model):
    # name = models.CharField(blank=False, max_length=40)
    port = models.IntegerField(blank=False, unique=True)
    cport = models.IntegerField(blank=False, unique=True)
    is_busy = models.BooleanField(default=False)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)

    def run(self):
        pass

    def get_port(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0

    def save(self, *args, **kwargs):

        super(Container, self).save(*args, **kwargs)

class Region(models.Model):
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    region_index = models.CharField(max_length=2, blank=False)
    has_more = models.BooleanField(default=True)
    parsed = models.BooleanField(default=False)


class PortInUse(models.Model):
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    port = models.IntegerField()
