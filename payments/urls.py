from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.payments_list, name='payments_list'),
    path('<int:id>/',views.payment_by_id, name='payment_by_id'),
    path('obligeds/',views.obligeds_list, name='obligeds_list'),
    path('obliged/<int:id>/',views.obliged_by_id, name='obliged_by_id'),
    path('history/',views.history, name='history'),
]
