# Views for this app
from apps.clinics.models import Clinic

def create_clinic(name, subscriber, timezone="UTC"):
    return Clinic.objects.create(
        name=name,
        subscriber=subscriber,
        timezone=timezone,
        is_active=True
    )