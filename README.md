# 📦 My Celery Project

A Django project configured with **Celery**, **Redis broker**,
**Periodic tasks via django-celery-beat**, and **result backend via
django-celery-results**.

This project demonstrates how to build a production-ready asynchronous
task processing system using Django and Celery.

------------------------------------------------------------------------

## 🚀 Features

-   ✅ Django + Celery integration
-   ✅ Redis as message broker
-   ✅ Task result storage in Django database
-   ✅ Periodic task scheduling using django-celery-beat
-   ✅ Admin interface for managing scheduled tasks
-   ✅ Example tasks (add, minus, clear cache)

------------------------------------------------------------------------

## 🛠 Tech Stack

  Component               Purpose
  ----------------------- ------------------------------------
  Django                  Web framework
  Celery                  Background task queue
  Redis                   Message broker
  django-celery-beat      Periodic task scheduler (DB-based)
  django-celery-results   Task result backend

------------------------------------------------------------------------

## 📥 Installation

Clone the repository:

``` bash
git clone https://github.com/aranya-code/my_celery_project.git
cd my_celery_project
```

Create virtual environment:

``` bash
python -m venv myenv
myenv\Scripts\activate  # Windows
# OR
source myenv/bin/activate  # Mac/Linux
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ⚙️ Configuration

Ensure Redis is running:

``` bash
redis-server
```

In `settings.py`:

``` python
INSTALLED_APPS = [
    'myapp',
    'django_celery_results',
    'django_celery_beat',
]

CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
```

------------------------------------------------------------------------

## 🗃 Apply Migrations

``` bash
python manage.py migrate
```

------------------------------------------------------------------------

## ▶️ Running the Project

### 1️⃣ Start Django

``` bash
python manage.py runserver
```

### 2️⃣ Start Celery Worker

``` bash
celery -A celeryproject worker -l info --pool=solo
```

### 3️⃣ Start Celery Beat (Database Scheduler)

``` bash
celery -A celeryproject beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

------------------------------------------------------------------------

## 📆 Periodic Tasks (Admin Panel)

Access Django admin:

    http://127.0.0.1:8000/admin/

You can manage periodic tasks from:

    django_celery_beat → Periodic Tasks

------------------------------------------------------------------------

## 📊 Monitoring Results

Task results are stored in the database and viewable in:

    django_celery_results → Task Results

------------------------------------------------------------------------

## 📂 Project Structure

    my_celery_project/
    │
    ├── celeryproject/
    │   ├── __init__.py
    │   ├── celery.py
    │   └── settings.py
    │
    ├── myapp/
    │   ├── tasks.py
    │   ├── views.py
    │   └── models.py
    │
    ├── manage.py
    └── requirements.txt

------------------------------------------------------------------------
