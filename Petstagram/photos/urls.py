from django.urls import path, include

from photos import views
app_name = 'photos'
urlpatterns = [
    path('add/',views.photo_add, name='add'),
    path('<int:pk>',include([
        path('',views.photo_detail, name='detail'),
        path('edit/',views.photo_edit, name='edit'),
    ]))
]