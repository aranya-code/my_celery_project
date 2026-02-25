from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

@shared_task(name='Subtract_Two_Numbers')
def minus(x, y):
    return x-y


@shared_task(name='Clear_Cache')
def clear_session_cache(id):
    print(f'Cache id: {id}')
    return id

@shared_task
def clear_redis(key):
    return key


#Create a schedule every 20 seconds
schedule, created = IntervalSchedule.objects.get_or_create(
    every = 20,
    period = IntervalSchedule.SECONDS,

)

#Schedule the periodic task
PeriodicTask.objects.get_or_create(
    name = 'Clear Redis data',
    task = 'myapp.tasks.clear_redis',
    interval = schedule,
    args = json.dumps(['hello'])
)