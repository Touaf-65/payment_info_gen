from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bill-home'),
    path('about/', views.about, name='bill-about'),
]
