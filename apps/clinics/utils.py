from django.http import HttpResponseForbidden
from django.shortcuts import redirect


def require_subscriber(view_func):
    def wrapper(request, *args, **kwargs):
        clinic = kwargs.get('clinic')
        if clinic.subscriber != request.user:
            return HttpResponseForbidden("Only the subscriber can perform this action.")
        return view_func(request, *args, **kwargs)
    return wrapper

@require_subscriber
def cancel_clinic(request, clinic):
    clinic.is_active = False
    clinic.save()
    return redirect('clinic_dashboard')