from django.shortcuts import render, get_object_or_404
from .models import Payment

def payments_list(request):
    payments_list = Payment.objects.all()
    context = {
        'payments_list': payments_list,
    }
    return render(request, 'payments/home.html', context)


def payment_by_id(request, id):
    payment = get_object_or_404(Payment, id=id)
    context = {
        'payment': payment,
    }
    return render(request, 'payments/payment.html', context)
