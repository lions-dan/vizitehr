from .base import *

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com']

CSRF_TRUSTED_ORIGINS = ['https://yourdomain.com']

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Configure production email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')

# Stripe and other API keys from env vars
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')