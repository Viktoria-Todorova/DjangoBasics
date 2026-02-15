from django.urls import path

from reviews import views
app_name = 'reviews'
urlpatterns = [
    path('', views.ReviewListView.as_view(), name='review-list'),
    path('create/',views.ReviewCreateView.as_view(),name='create'),
]