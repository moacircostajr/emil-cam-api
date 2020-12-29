from django.db import models
import uuid

from companies.models import Company


class Settings (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=True)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=True)
    business_name = models.CharField(max_length=60, null=True, blank=False)
    platform_name = models.CharField(max_length=100, null=False, blank=True)
    page_title = models.CharField(max_length=100, null=False, blank=True)
    page_description = models.CharField(max_length=200, null=False, blank=True)
    email_default_answer = models.EmailField(null=False, blank=True)
    email_contact = models.EmailField(null=False, blank=True)
    email_alert = models.EmailField(null=False, blank=True)
    alert_online = models.IntegerField(null=True, blank=True)
    alert_offline = models.IntegerField(null=True, blank=True)
    site = models.CharField(max_length=200, null=False, blank=True)
    custom_domain = models.CharField(max_length=200, null=False, blank=True)
    primary_color = models.CharField(max_length=20, null=False, blank=True)
    secondary_color = models.CharField(max_length=20, null=False, blank=True)
    all_cameras = models.BooleanField(default=True)
    advertising = models.BooleanField(default=True)
    recording_plan = models.IntegerField(null=True, blank=True)
    daily_synthesis = models.BooleanField(default=True)
    terms_use = models.TextField(blank=True)
    privacity_policy = models.TextField(blank=True)
    #"permissao_disparo_alerta": true,
    #"permissao_alterar_email_login": true,
    #"permissao_usuarios_anonimos": true,
    #"cameras_publicas": true,
    #"lpr_c_whitelist": true,
    #"customizacao_campos_clientes": [{"id": "DESAB"}, {"cpf": "OBRIG"}, {"cep": "HABIL"}],
    creation = models.DateTimeField(auto_now_add=True)
