from django.contrib.auth.models import User
from django.db import models
from django.db.models import DateTimeField
from django.db.models import ForeignKey


class Auditable(models.Model):
    created_date = DateTimeField(auto_created=True)
    modified_date = DateTimeField(auto_now=True)
    created_user = ForeignKey(User, related_name="created_user")
    modified_user = ForeignKey(User, related_name="modified_user")

    class Meta:
        abstract = True
