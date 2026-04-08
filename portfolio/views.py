from django.http import JsonResponse, Http404
from django.shortcuts import render

from .data import CASE_STUDIES, METRICS, PIPELINE_STEPS, aggregate_snapshot


def home(request):
    snapshot = aggregate_snapshot()
    featured = CASE_STUDIES[0]
    return render(
        request,
        "portfolio/home.html",
        {
            "case_studies": CASE_STUDIES,
            "metrics": METRICS,
            "featured": featured,
            "pipeline_steps": PIPELINE_STEPS,
            "snapshot": snapshot,
        },
    )


def case_study_detail(request, slug):
    case_study = next((item for item in CASE_STUDIES if item["slug"] == slug), None)
    if not case_study:
        raise Http404("Case study not found.")
    return render(
        request,
        "portfolio/case_study.html",
        {
            "case_study": case_study,
            "related": [item for item in CASE_STUDIES if item["slug"] != slug][:2],
        },
    )


def api_snapshot(request):
    return JsonResponse(
        {
            "platform": "DataOps Portfolio Backend",
            "snapshot": aggregate_snapshot(),
            "metrics": METRICS,
        }
    )


def api_case_studies(request):
    return JsonResponse({"items": CASE_STUDIES})
