from django.urls import path
from api_index import views
app_name = 'api_index'

urlpatterns = [
    path('', views.index),
    path('en_de/', views.en_de),
    path('transform_api_sign/', views.to_transform_api_sign)
]