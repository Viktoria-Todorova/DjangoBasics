from django.shortcuts import render
from datetime import datetime

# Create your views here.
def show_current_time(request):
    context = {
        'current_time': datetime.now()
    }
    return render(request, 'current_time.html', context)