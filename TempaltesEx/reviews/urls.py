from django.urls import path

from reviews.views import recent_reviews, review_detail

app_name = 'reviews'

urlpatterns = [
    path('recent/', recent_reviews, name='recent'),
    path('<int:pk>/', review_detail, name='detail'),
]