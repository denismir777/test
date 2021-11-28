from celery import group
from celery import shared_task

@shared_task
def simple_print(i):
    print(i)

res = group(simple_print(i) for i in range(10))()
