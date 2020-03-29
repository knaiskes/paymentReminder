from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment, Obliged
from .forms import DateHistorySearchForm

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

def history(request):
    payments_history_list = []
    form = DateHistorySearchForm(request.POST or None)

    range_options = {
        #TODO: import date and use its functions rather than hard coded values
        'week': 7,'month': 30, 'two_months': 60, 'three_months': 90
    }

    if form.is_valid():
        import datetime

        today = datetime.date.today()

        try:
            selected_option = range_options[form.cleaned_data['days']]
        except(KeyError):
            selected_option = today
        print(selected_option)

        context = { 'payments_history_list': payments_history_list, }
        redirect('payments/history.html', context)

    context = {
        #'payments_history_list': payments_history_list,
        'form': form,
    }

    return render(request, 'payments/history.html', context)
