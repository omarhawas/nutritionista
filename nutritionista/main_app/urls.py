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
    path('foods/', views.FoodList.as_view(), name='foods_index'),
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name='foods_detail'),
    path('foods/create/', views.FoodCreate.as_view(), name='foods_create'),
    path('foods/<int:pk>/update', views.FoodUpdate.as_view(), name='foods_update'),
    path('foods/<int:pk>/delete', views.FoodDelete.as_view(), name='foods_delete'),
]