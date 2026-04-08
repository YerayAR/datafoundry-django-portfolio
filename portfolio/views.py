from django.db.utils import OperationalError, ProgrammingError
from django.http import Http404, JsonResponse
from django.shortcuts import render

from .data import CASE_STUDIES, METRICS, PIPELINE_STEPS, aggregate_snapshot
from .models import CaseStudy, Metric, PipelineStep

def serialize_case_study(case_study):
    return {
        "slug": case_study.slug,
        "title": case_study.title,
        "tag": case_study.tag,
        "summary": case_study.summary,
        "problem": case_study.problem,
        "solution": case_study.solution,
        "impact": {
            "hours_saved_month": case_study.hours_saved_month,
            "accuracy_gain": case_study.accuracy_gain,
            "throughput_gain": case_study.throughput_gain,
        },
        "stack": list(case_study.stack.values_list("name", flat=True)),
        "timeline": case_study.timeline,
    }


def get_case_studies():
    try:
        if CaseStudy.objects.exists():
            queryset = CaseStudy.objects.prefetch_related("stack")
            return [serialize_case_study(case_study) for case_study in queryset]
    except (OperationalError, ProgrammingError):
        pass
    return CASE_STUDIES


def get_metrics():
    try:
        if Metric.objects.exists():
            return [{"label": item.label, "value": item.value} for item in Metric.objects.all()]
    except (OperationalError, ProgrammingError):
        pass
    return METRICS


def get_pipeline_steps():
    try:
        if PipelineStep.objects.exists():
            return [item.description for item in PipelineStep.objects.all()]
    except (OperationalError, ProgrammingError):
        pass
    return PIPELINE_STEPS


def home(request):
    case_studies = get_case_studies()
    metrics = get_metrics()
    pipeline_steps = get_pipeline_steps()
    snapshot = aggregate_snapshot(case_studies)
    featured = case_studies[0]
    return render(
        request,
        "portfolio/home.html",
        {
            "case_studies": case_studies,
            "metrics": metrics,
            "featured": featured,
            "pipeline_steps": pipeline_steps,
            "snapshot": snapshot,
        },
    )


def case_study_detail(request, slug):
    case_studies = get_case_studies()
    case_study = next((item for item in case_studies if item["slug"] == slug), None)
    if not case_study:
        raise Http404("Case study not found.")
    return render(
        request,
        "portfolio/case_study.html",
        {
            "case_study": case_study,
            "related": [item for item in case_studies if item["slug"] != slug][:2],
        },
    )


def api_snapshot(request):
    case_studies = get_case_studies()
    return JsonResponse(
        {
            "platform": "DataOps Portfolio Backend",
            "snapshot": aggregate_snapshot(case_studies),
            "metrics": get_metrics(),
        }
    )


def api_case_studies(request):
    return JsonResponse({"items": get_case_studies()})
