# DataFoundry

`DataFoundry` is a Django portfolio project focused on backend thinking, data workflows, and analytics delivery. It is designed as a portfolio piece that looks polished for recruiters while also exposing enough structure to demonstrate Python, Django, template composition, and API design.

## What it includes

- Cinematic landing page for a data/backend portfolio
- Django-rendered case study pages
- Public JSON endpoints for metrics and project data
- Reusable content model stored in Python dictionaries
- Vercel-ready deployment setup

## Routes

- `/` home page
- `/case-study/<slug>/` case study detail
- `/api/snapshot/` aggregated portfolio metrics
- `/api/case-studies/` structured case study feed

## Stack

- Python
- Django
- WhiteNoise
- HTML templates
- Vanilla CSS and JavaScript
- Vercel

## Local run

```powershell
pip install -r requirements.txt
python manage.py runserver
```

## Why this project exists

This portfolio is meant to show a stronger backend profile than a static one-page site. It presents project outcomes, process design, and API output in one deployable Django app that can be shown publicly.
