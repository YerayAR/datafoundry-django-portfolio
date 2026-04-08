import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from portfolio.models import Technology, CaseStudy, Metric, PipelineStep
from portfolio.data import CASE_STUDIES, METRICS, PIPELINE_STEPS

def run():
    print("Populating database...")
    
    # 1. Populate Pipeline Steps
    PipelineStep.objects.all().delete()
    for idx, step_desc in enumerate(PIPELINE_STEPS):
        PipelineStep.objects.create(description=step_desc, order=idx)
    print("Pipeline steps added.")

    # 2. Populate Metrics
    Metric.objects.all().delete()
    for idx, metric in enumerate(METRICS):
        Metric.objects.create(label=metric["label"], value=metric["value"], order=idx)
    print("Metrics added.")

    # 3. Populate Case Studies
    CaseStudy.objects.all().delete()
    Technology.objects.all().delete()
    
    for item in CASE_STUDIES:
        case = CaseStudy.objects.create(
            title=item["title"],
            slug=item["slug"],
            tag=item["tag"],
            summary=item["summary"],
            problem=item["problem"],
            solution=item["solution"],
            timeline=item["timeline"],
            hours_saved_month=item["impact"]["hours_saved_month"],
            accuracy_gain=item["impact"]["accuracy_gain"],
            throughput_gain=item["impact"]["throughput_gain"]
        )
        
        for tech_name in item["stack"]:
            tech, created = Technology.objects.get_or_create(name=tech_name)
            case.stack.add(tech)
            
    print("Case studies added.")
    print("Done!")

if __name__ == '__main__':
    run()
