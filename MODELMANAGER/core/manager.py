from django.db.models.manager import Manager
from django.db import models

class custom_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
