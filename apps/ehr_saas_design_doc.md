
# EHR SaaS System - Design Documentation

## Overview

This project is a modular, multi-tenant EHR SaaS platform designed for clinics, providers, and patients. It supports advanced healthcare workflows including patient charting, scheduling, AI automation, secure messaging, billing, and interoperability.

---

## Core Features

### Clinic Management
- Clinics can sign up and configure their settings via a guided onboarding flow.
- Clinics can invite users with roles like Admin, Provider, Staff, and Biller.
- Clinics can add patients and bill them directly.

### Multi-Tenant Access
- Clinics are treated as tenants.
- Patients and users are scoped to clinics via join tables.
- Clinics can only access their own data.

### Patient Management
- Patients can be added by clinics using email/phone.
- Patients can receive a magic link to register or connect to a new clinic.
- Patients can belong to multiple clinics and access their records via a unified portal.

### Role-Based Access
- Roles (Admin, Provider, Biller, Staff) are managed via ClinicUser model.
- Permissions are checked at the clinic level.
- Middleware blocks access if a clinic is inactive or a user is unauthorized.

### Billing
- Stripe subscription for clinic activation.
- Stripe Payment Links for patient billing (copays, invoices).
- Lockout clinics if payment is overdue for 5+ days.

### Secure Messaging
- HIPAA-compliant direct messages between providers and patients.
- Broadcast messages from clinics to all their patients.
- Message delivery via in-app, email, or SMS (Twilio).

### Analytics
- Clinics can view dashboards showing:
  - Patient count
  - Appointment stats
  - Monthly income
  - Active provider metrics

### EHR Core Modules
- Charting (SOAP notes, templates)
- Scheduling (provider calendar, patient appointments)
- Orders & Results (labs, imaging)
- Clinical Decision Support (alerts, suggestions)
- Portal (patient access to documents, requests)

### AI & Automation
- AI engine for:
  - Note summarization
  - Billing code suggestions
  - Smart scheduling
- LLM/ML models integrated via LangChain, OpenAI, or local inference

### Interoperability
- FHIR-ready API structure
- External lab, pharmacy, or system integration via `interop` app

### Security
- HIPAA-compliant data handling
- Role-based permissions
- Encrypted messaging
- Audit logging of sensitive actions

---

## Project Structure

```
vizitehr/
├── apps/
│   ├── core/                   # User model, shared mixins
│   ├── accounts/               # Auth & registration
│   ├── clinics/                # Clinic profile and settings
│   ├── clinic_users/           # Role management
│   ├── patients/               # Patient profile & clinic joins
│   ├── patient_portal/         # Patient self-service area
│   ├── billing/                # Clinic Stripe subscription
│   ├── patient_payments/       # Charges & Stripe links for patients
│   ├── ehr/
│   │   ├── charting/           # SOAP notes, documents
│   │   ├── scheduling/         # Appointments, calendars
│   │   ├── portal/             # Patient forms, summaries
│   │   ├── orders/             # Lab & medication orders
│   │   ├── results/            # Result management
│   │   ├── support/            # Clinical decision logic
│   ├── ai_engine/              # LLM-driven automation
│   ├── messaging/              # Secure chat & notifications
│   ├── analytics/              # Clinic dashboards
│   ├── interop/                # FHIR / HL7 data APIs
│   ├── auditlog/               # Event tracking
│   ├── onboarding/             # Clinic setup wizard
├── config/                     # Django settings
├── templates/                  # Shared templates
├── api/                        # DRF-based API structure
├── static/                     # Frontend assets
├── manage.py
```

---

## Next Steps

- Implement custom user model in `core`
- Build out onboarding + billing flows
- Wire Stripe and Twilio integrations
- Build patient portal templates
