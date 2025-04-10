# Models for this app
from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class User(AbstractUser):
    # Additional fields
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    timezone = models.CharField(max_length=50, default='UTC')

    def has_clinic_role(self, clinic, role: str) -> bool:
        """Check if user has a specific role in a given clinic"""
        return self.groups.filter(name=f"{clinic.id}_{role}").exists()

    def assign_clinic_role(self, clinic, role: str):
        """Assign user to a group like '3_admin' (clinic 3, role admin)"""
        group_name = f"{clinic.id}_{role}"
        group, _ = Group.objects.get_or_create(name=group_name)
        self.groups.add(group)

    def remove_clinic_role(self, clinic, role: str):
        """Remove the user from a specific clinic's role group"""
        group_name = f"{clinic.id}_{role}"
        group = Group.objects.filter(name=group_name).first()
        if group:
            self.groups.remove(group)

    def get_roles_for_clinic(self, clinic) -> list:
        """List all roles this user has within a clinic"""
        return [
            group.name.split("_", 1)[1]
            for group in self.groups.filter(name__startswith=f"{clinic.id}_")
        ]

