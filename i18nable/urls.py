from django.urls import path
from some_app import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
