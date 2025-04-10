# Models for this app
from django.db import models

class AgentConversation(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    clinic = models.ForeignKey('clinics.Clinic', on_delete=models.CASCADE)
    input_text = models.TextField()
    response_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']