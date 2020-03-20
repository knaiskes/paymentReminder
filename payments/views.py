from django.shortcuts import render, get_object_or_404
from .models import Payment

def HomeView(request):
    payments_list = Payment.objects.all()
    context = {
        'payments_list': payments_list,
    }
    return render(request, 'payments/home.html', context)
