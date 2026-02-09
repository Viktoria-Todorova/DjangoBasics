
from django.urls import path

from travelers import views

urlpatterns = [
    path('create/',views.TravelerView.as_view(),name='create'),
    path('update/<int:pk>/',views.TravelerUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.TravelerDeleteView.as_view(),name='delete'),
]