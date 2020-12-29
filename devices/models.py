from companies.models import Company
from django.db import models
import pytz
import uuid

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=True)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=True)
    business_name = models.CharField(max_length=60, null=True, blank=False)
    device = models.CharField(max_length=100, null=False, blank=False)
    model = models.CharField(max_length=60, null=False, blank=False)
    access_address = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=False)
    complement = models.CharField(max_length=60, null=True, blank=True)
    neighborhood = models.CharField(max_length=60, null=True, blank=False)
    city = models.CharField(max_length=60, null=True, blank=False)
    state = models.CharField(max_length=60, null=True, blank=False)
    country = models.CharField(max_length=60, null=True, blank=False)
    time_zone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC', null=True, blank=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=6, null=False, blank=False)
    longitude = models.DecimalField(max_digits=11, decimal_places=6, null=False, blank=False)
    sensibility = models.IntegerField(default=1, null=False, blank=True)
    is_active = models.BooleanField(null=False, blank=False, default=False)
    creation = models.DateTimeField(auto_now_add=True)
