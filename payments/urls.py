from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.HomeView, name='HomeView'),
    path('<int:id>/',views.payment_by_id, name='payment_by_id'),
]
