
from django.urls import path

from travelers import views
app_name = 'travelers'

urlpatterns = [
    path('', views.TravelerListView.as_view(), name='traveler_list'),
    path('create/',views.TravelerView.as_view(),name='create'),
    path('update/<int:pk>/',views.TravelerUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.TravelerDeleteView.as_view(),name='delete'),
    path('<int:pk>/',views.TravelerDetailView.as_view(),name='detail'),
]