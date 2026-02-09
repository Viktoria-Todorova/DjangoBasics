from django.urls import path

from reviews import views

urlpatterns = [
    path('create/',views.ReviewCreateView.as_view(),name='create'),
]