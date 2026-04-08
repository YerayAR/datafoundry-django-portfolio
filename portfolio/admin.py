from django.contrib import admin
from .models import Technology, CaseStudy, Metric, PipelineStep

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'timeline', 'hours_saved_month')
    search_fields = ('title', 'tag')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('stack',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order')
    list_editable = ('value', 'order')

@admin.register(PipelineStep)
class PipelineStepAdmin(admin.ModelAdmin):
    list_display = ('description', 'order')
    list_editable = ('order',)
