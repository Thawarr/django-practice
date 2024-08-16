from django.db import models
from django.utils import timezone

# Create your models here.
class Tenant(models.Model):
  TENANT_TYPE_CHOICES = [
    ('AND', 'Android App'),
    ('IOS', 'IOS App'),
    ('WIN', 'Windows'),
    ('A&I', 'Android And IOS'),
    ('ALL', 'All Apps'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='tenantsLogos/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=3, choices=TENANT_TYPE_CHOICES, default='ALL')
  description = models.TextField(default='')

  def __str__(self):
    return self.name