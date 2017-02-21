from celery import shared_task
from app.models import Test


@shared_task
def create(data):
    return Test.objects.create(name=data)
