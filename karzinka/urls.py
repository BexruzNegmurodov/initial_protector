from django.urls import path
from .views import home, detail, create, edit, delete

app_name = 'karzinka'

urlpatterns = [
    path('', home, name='home'),
    path('detail/<slug:slug>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete_page/<int:pk>/', delete, name='delete')
]

