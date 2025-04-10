# Models for this app
from django.db import models
from django.conf import settings

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='subscribed_clinics'
    )
    timezone = models.CharField(max_length=50, default='UTC')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name