from django.contrib import admin
from .models import Organization, Container, Broker
# Register your models here.

admin.site.register(Organization)
admin.site.register(Container)
admin.site.register(Broker)