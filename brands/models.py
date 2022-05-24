from django.db import models
from closets.models import *
from user.models import *

# Create your models here.
class Brand(models.Model):
    admin = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    admit = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    site = models.URLField(max_length=200, null=True)
    photo = models.ImageField(blank=False, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name