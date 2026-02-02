from django.urls import path, include

from reviews.views import recent_reviews, review_detail, review_create, review_edit, review_delete, review_bulk_update

app_name = 'reviews'

urlpatterns = [
    path('recent/', recent_reviews, name='recent-reviews'),
    path('create/', review_create, name='create'),
    path('<slug:book_slug>',review_bulk_update,name='update'),
    path('<int:pk>/', include([
        path('',review_detail, name='detail'),
        path('edit/', review_edit, name='edit'),
        path('delete/', review_delete, name='delete'),
    ]))

]
