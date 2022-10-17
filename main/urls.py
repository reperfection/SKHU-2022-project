from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.main, name='main'),
    path('', include('it.urls'))
]