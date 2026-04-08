from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("case-study/<slug:slug>/", views.case_study_detail, name="case-study"),
    path("api/snapshot/", views.api_snapshot, name="api-snapshot"),
    path("api/case-studies/", views.api_case_studies, name="api-case-studies"),
]
