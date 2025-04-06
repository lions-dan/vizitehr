# 🛠️ EHR SaaS Config Folder Documentation

The `config/` directory contains the core configuration for your Django EHR SaaS platform, including settings for development, production, and shared/base logic.

---

## 📁 Folder Structure

```
config/
├── __init__.py        # Optional autoload logic or empty
├── base.py            # Shared settings for all environments
├── dev.py             # Development-specific settings
├── prod.py            # Production-specific settings
```

---

## 🔧 config/base.py

This file holds the **shared settings** used by both development and production environments.

### Key responsibilities:
- Project directory paths
- Installed apps
- Middleware
- Templates
- Static and media file settings
- DRF and authentication settings
- Custom user model

Use this as the foundation to keep environment-specific files clean and focused.

---

## 🧪 config/dev.py

This file holds **development-specific settings** and inherits from `base.py`.

### Includes:
- `DEBUG = True`
- `ALLOWED_HOSTS = ['*']`
- Console email backend for testing
- Open CORS policy for local testing

Use this for local development, testing, and staging environments.

---

## 🚀 config/prod.py

This file holds **production-specific settings** and inherits from `base.py`.

### Includes:
- `DEBUG = False`
- Secure cookie and CSRF settings
- Real email backend (e.g., SendGrid)
- Stripe and API keys from environment variables
- Domain restrictions and trusted origins

Always ensure secure and performance-friendly settings in production.

---

## 🔁 Switching Environments

You can run Django with a specific settings file using the `DJANGO_SETTINGS_MODULE` environment variable:

```bash
# For development
DJANGO_SETTINGS_MODULE=config.dev python manage.py runserver

# For production
DJANGO_SETTINGS_MODULE=config.prod gunicorn ehr_saas.wsgi
```

---

## 📌 Best Practices

- Never hard-code secrets in these files; use environment variables.
- Keep `base.py` lean and focused on logic shared across all environments.
- Use `.env` or secret managers in production to inject variables.

---

## ✅ Summary

| File        | Purpose                            |
|-------------|-------------------------------------|
| `base.py`   | Common/shared settings              |
| `dev.py`    | Development/local-only config       |
| `prod.py`   | Production config (secure, strict)  |
| `__init__.py` | Optional auto-load or empty        |