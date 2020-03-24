from django.shortcuts import render, get_object_or_404
from .models import Payment, Obliged

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

def obligeds_list(request):
    obligeds_list = Obliged.objects.all()
    context = {
        'obligeds_list': obligeds_list,
    }
    return render(request, 'payments/obligeds.html', context)

def obliged_by_id(request, id):
    obliged = get_object_or_404(Obliged, id=id)
    payments_list = Payment.objects.filter(obliged=id)
    context = {
        'obliged': obliged,
        'payments_list': payments_list
    }
    return render(request, 'payments/obliged.html', context)
