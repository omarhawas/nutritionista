from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('days/', views.days_index, name='index'),
    path('days/<int:day_id>/', views.days_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('days/create/', views.DayCreate.as_view(), name='days_create'),
    path('days/<int:pk>/update/', views.DayUpdate.as_view(), name='days_update'),
    path('days/<int:pk>/delete/', views.DayDelete.as_view(), name='days_delete'),
]