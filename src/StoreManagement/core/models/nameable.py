from django.db import models
from django.db.models import CharField


class Nameable(models.Model):
    name = CharField(max_length=150, blank=True, null=False)

    class Meta:
        abstract = True
