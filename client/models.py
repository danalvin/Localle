from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.


class man(models.Model):
    Name = models.CharField(max_length=25)
    Location = PlainLocationField(based_fields=['city'], zoom=7)
    