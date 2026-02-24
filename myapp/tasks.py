from celery import shared_task

@shared_task(name='Subtract_Two_Numbers')
def minus(x, y):
    return x-y