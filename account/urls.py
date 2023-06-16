from django.urls import path
from .views import mylogin, mylogout, myregister

app_name = 'account'

urlpatterns = [
    path('login/', mylogin, name='login'),
    path('logout/', mylogout, name='logout'),
    path('register/', myregister, name='register')
]
