from django.urls import path
from base_tools import views
app_name = 'base_tools'

urlpatterns = [
    path('en_de_index/', views.en_de_index),
    path('deciphering/', views.deciphering),
    path('encryption/', views.encryption),
]