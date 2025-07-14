---

## ✅ System Design & Architecture Documentation

### System Architecture Overview
```markdown
1. **Frontend (React + Redux + Recharts)**
   - Provides the user interface for dashboards, analytics, and reports.

2. **Backend (Django + Django REST Framework)**
   - Exposes REST APIs for all functionalities.
   - Handles authentication, data processing, and business logic.

3. **Database (PostgreSQL)**
   - Stores all persistent data including users, assessments, vulnerabilities, threats, audit logs.

4. **Task Queue (Celery + Redis)**
   - Handles asynchronous tasks like vulnerability scans, threat data fetching.

5. **Monitoring & Logging**
   - Tools like Sentry for error tracking.
   - Suricata for Intrusion Detection.

6. **DevOps**
   - Dockerized services.
   - CI/CD pipelines via GitHub Actions.
```