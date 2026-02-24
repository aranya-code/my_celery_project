from django.shortcuts import render
from celeryproject.celery import add
from myapp.tasks import minus
from celery.result import AsyncResult

# Create your views here.
def home(request):
    result1 = add.delay(10, 20)
    return render(request, 'myapp/home.html',{'result1': result1, 'task_id': result1.id})

def about(request):
    result2 = minus.apply_async(args=[45, 36])    
    return render(request, 'myapp/about.html', {'result2': result2})

def contact(request):
    return render(request, 'myapp/contact.html')

def check_result(request, task_id):
    result = AsyncResult(task_id)
    return render(request, 'myapp/task_data.html', {'result': result})
    

