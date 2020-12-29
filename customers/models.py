from companies.models import Company
from django.db import models
import pytz
import uuid

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
    id_company = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=True)
    business_name = models.CharField(max_length=60, null=True, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False)
    address = models.CharField(max_length=60, null=False, blank=False)
    complement = models.CharField(max_length=60, null=True, blank=True)
    neighborhood = models.CharField(max_length=60, null=False, blank=False)
    city = models.CharField(max_length=60, null=False, blank=False)
    state = models.CharField(max_length=60, null=False, blank=False)
    country = models.CharField(max_length=60, null=False, blank=False)
    time_zone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC', null=True, blank=True)
    zip_code = models.CharField(max_length=8, null=False, blank=False)
    latitude = models.DecimalField(max_digits=11, decimal_places=6)
    longitude = models.DecimalField(max_digits=11, decimal_places=6)
    phones = models.CharField(max_length=60, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    is_active = models.BooleanField(null=False, blank=False, default=True)
    creation = models.DateTimeField(auto_now_add=True)