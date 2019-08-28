from django.urls import path
from browser_api import views
app_name = 'browser_api'

urlpatterns = [
    path('api_sign/', views.api_sign_index),
    path('transform_api_sign/', views.transform_api_sign),
]