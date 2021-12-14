from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('days/', views.days_index, name='index'),
    path('days/<int:day_id>/', views.days_detail, name='detail'),
]