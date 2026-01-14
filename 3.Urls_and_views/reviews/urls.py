from django.urls import path, re_path

from reviews.views import recent_review, review_detail, review_by_year

app_name = 'review'
urlpatterns = [
    path('',recent_review, name ='list'),
    re_path(r'^(?P<year>20\d{2})/$',review_by_year,name= 'list-year'), #re_path!!!!!!!!!
    path('details/<int:pk>/', review_detail, name ='detail'),

]
