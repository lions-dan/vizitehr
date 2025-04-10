from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Clinic

@receiver(post_save, sender=Clinic)
def setup_clinic_roles(sender, instance, created, **kwargs):
    if created:
        clinic_id = instance.id
        role_names = ['admin', 'provider', 'staff', 'biller']

        for role in role_names:
            group_name = f"{clinic_id}_{role}"
            Group.objects.get_or_create(name=group_name)

        if instance.subscriber:
            admin_group = Group.objects.get(name=f"{clinic_id}_admin")
            instance.subscriber.groups.add(admin_group)