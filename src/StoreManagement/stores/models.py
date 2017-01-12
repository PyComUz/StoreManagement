from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey

from core.models.auditable import Auditable
from core.models.nameable import Nameable


class Store(Auditable, Nameable, models.Model):
    responsible_employee = ForeignKey(User, related_name="responsible_employee", null=True)

    class Meta:
        abstract = False
