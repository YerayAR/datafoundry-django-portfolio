from django.db import models
from django.utils.text import slugify

class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.name

class CaseStudy(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    tag = models.CharField(max_length=100)
    summary = models.TextField()
    problem = models.TextField()
    solution = models.TextField()
    timeline = models.CharField(max_length=50)
    
    # Impact Metrics fields
    hours_saved_month = models.IntegerField(default=0, help_text="Number of hours saved per month")
    accuracy_gain = models.FloatField(default=0.0, help_text="Percentage of accuracy gained")
    throughput_gain = models.FloatField(default=0.0, help_text="Percentage of workflow throughput gain")
    
    stack = models.ManyToManyField(Technology, related_name="case_studies")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Case Studies"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Metric(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.label

class PipelineStep(models.Model):
    description = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Step {self.order}: {self.description}"
