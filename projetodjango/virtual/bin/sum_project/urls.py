from django.urls import path
from sum_app import views

urlpatterns = [
    path('', views.result_page, name='result_page'),  # Rota vazia para renderizar result.html
    path('sum/', views.sum_numbers, name='sum_numbers'),
]
