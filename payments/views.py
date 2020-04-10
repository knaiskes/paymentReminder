from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment, Obliged
from .forms import DateHistorySearchForm

def payments_list(request):
    import datetime
    # Get current week's payments
    today = datetime.date.today()
    week_start = today - datetime.timedelta(days=today.weekday())
    week_end = week_start + datetime.timedelta(days=6)

    payments_list = Payment.objects.filter(
        date__range=[week_start, week_end]
    )
    context = {
        'payments_list': payments_list,
        'today': today,
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

    if form.is_valid():
        import datetime
        today = datetime.date.today()

        if form.get_selected_option() != today:
            search_range = today + datetime.timedelta(- form.get_selected_option())

            payments_history_list = Payment.objects.filter(
                date__range=[search_range, today])

        context = { 'payments_history_list': payments_history_list, }

        redirect('payments/history.html', context)

    context = {
        'payments_history_list': payments_history_list,
        'form': form,
    }

    return render(request, 'payments/history.html', context)
