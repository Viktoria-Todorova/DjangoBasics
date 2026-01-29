from django.urls import path

from reviews.views import recent_reviews, review_detail, review_create, review_edit, review_delete

app_name = 'reviews'

urlpatterns = [
    path('recent/', recent_reviews, name='recent'),
    path('<int:pk>/', review_detail, name='detail'),
    path('create/', review_create, name='create'),
    path('<int:pk>/edit/', review_edit, name='edit'),
    path('<int:pk>/delete/', review_delete, name='delete'),
]