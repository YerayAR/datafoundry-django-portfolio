from statistics import mean

CASE_STUDIES = [
    {
        "slug": "invoice-intelligence",
        "title": "Invoice Intelligence Pipeline",
        "tag": "ETL + OCR",
        "summary": "A backend automation flow for extracting invoice fields, validating records, and loading structured outputs into an operations database.",
        "problem": "Finance teams were manually transcribing invoice data and reconciling mismatches across spreadsheets and internal tools.",
        "solution": "I designed a Python pipeline with OCR extraction, schema validation, anomaly flags, and an operator review layer before persisting records.",
        "impact": {
            "hours_saved_month": 42,
            "accuracy_gain": 18,
            "throughput_gain": 61,
        },
        "stack": ["Python", "Django", "Pandas", "SQL", "OCR"],
        "timeline": "6 weeks",
    },
    {
        "slug": "demand-radar",
        "title": "Demand Radar Forecast Hub",
        "tag": "Forecasting",
        "summary": "A forecast monitoring experience for commercial teams combining trend snapshots, lead indicators, and delivery-risk scoring.",
        "problem": "The sales team had dashboards, but they were fragmented and did not surface future demand risks early enough.",
        "solution": "I built a backend-first portfolio case with scenario cards, forecast summaries, and a simple insights API that feeds the frontend in real time.",
        "impact": {
            "hours_saved_month": 31,
            "accuracy_gain": 12,
            "throughput_gain": 37,
        },
        "stack": ["Python", "Django", "Time Series", "SQL", "REST"],
        "timeline": "4 weeks",
    },
    {
        "slug": "retail-signal-ops",
        "title": "Retail Signal Ops Layer",
        "tag": "Analytics API",
        "summary": "A lightweight backend layer exposing portfolio-grade endpoints for KPIs, case studies, and operational health indicators.",
        "problem": "A portfolio can look visually strong and still fail to communicate backend thinking, API design, and data modeling discipline.",
        "solution": "I added API endpoints, structured data dictionaries, and reusable Django views to show that the product can evolve into a production analytics platform.",
        "impact": {
            "hours_saved_month": 19,
            "accuracy_gain": 9,
            "throughput_gain": 24,
        },
        "stack": ["Django", "Python", "JSON", "Templates", "Vercel"],
        "timeline": "3 weeks",
    },
]

METRICS = [
    {"label": "Automation Hours Saved", "value": "92h/mo"},
    {"label": "Average Accuracy Lift", "value": "+13%"},
    {"label": "Workflow Throughput Gain", "value": "+41%"},
    {"label": "Deployment Model", "value": "Django on Vercel"},
]

PIPELINE_STEPS = [
    "Ingest raw operational data",
    "Validate schema and detect anomalies",
    "Enrich records with business rules",
    "Expose insights through Django views and APIs",
    "Deliver dashboard-ready outputs",
]


def aggregate_snapshot(case_studies=None):
    source = case_studies or CASE_STUDIES
    hours = sum(item["impact"]["hours_saved_month"] for item in source)
    accuracy = round(mean(item["impact"]["accuracy_gain"] for item in source), 1)
    throughput = round(mean(item["impact"]["throughput_gain"] for item in source), 1)
    return {
        "hours_saved_month": hours,
        "average_accuracy_gain": accuracy,
        "average_throughput_gain": throughput,
        "projects": len(source),
    }
