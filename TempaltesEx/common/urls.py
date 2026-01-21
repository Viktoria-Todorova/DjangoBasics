from django.urls import path
from common.views import show_current_time

app_name = 'common'

urlpatterns = [
    path('current-time/', show_current_time, name='current_time'),
]