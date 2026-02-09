from django.urls import path, include

from common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('teen/', views.HomeTeenView.as_view(), name='home-teen'),
    path('age-check/', views.AgeCheckRedirectView.as_view(), name='age-check'),
]