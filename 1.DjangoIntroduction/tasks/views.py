from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from tasks.models import Task


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context = {
        'tasks' : Task.objects.all(),
    }
    return render(request, 'index.html', context)




def index2(request: HttpRequest) -> HttpResponse:
    all_tasks = Task.objects.all()
    template =[
        '<h1>All Tasks</h1>',
        *[f"<li>{t.title} - {t.is_complete}</li>" for t in all_tasks]
    ]
    return HttpResponse('\n'.join(template))




