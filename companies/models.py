from django.db import models
import uuid
import pytz

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class Company(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False)
	cnpj = models.CharField(max_length=14, null=True, blank=True)
	company_name = models.CharField(max_length=60, null=True, blank=True)
	business_name = models.CharField(max_length=60,  null=False, blank=False)
	address = models.CharField(max_length=60, null=False, blank=True)
	complement = models.CharField(max_length=60, null=True, blank=True)
	neighborhood = models.CharField(max_length=60, null=False, blank=False)
	city = models.CharField(max_length=60, null=False, blank=False)
	state = models.CharField(max_length=60, null=False, blank=False)
	country = models.CharField(max_length=60, null=False, blank=False)
	zip_code = models.CharField(max_length=8, null=False, blank=True)
	time_zone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC', null=True, blank=True)
	latitude = models.DecimalField(max_digits=11, decimal_places=6, null=True, blank=True)
	longitude = models.DecimalField(max_digits=11, decimal_places=6, null=True, blank=True)
	phones = models.CharField(max_length=60, null=True, blank=True)
	email = models.EmailField(null=False, blank=True)
	first_name_owner = models.CharField(max_length=60, null=False, blank=True)
	last_name_owner = models.CharField(max_length=60, null=False, blank=True)
	cpf_owner = models.CharField(max_length=11, null=False, blank=True)
	email_owner = models.EmailField(null=False, blank=True)
	id_owner = models.UUIDField(null=True, blank=True)
	is_active = models.BooleanField(null=False, blank=False, default=True)
	creation = models.DateTimeField(auto_now_add=True, blank=True)
