from django import forms

DAYS_CHOICES = (
    ('', '-----'),
    ('week', 'Week'),
    ('month', 'Month'),
    ('two_months', 'Two Months'),
    ('three_months', 'Three Months'),
)

class DateHistorySearchForm(forms.Form):
    days = forms.ChoiceField(choices = DAYS_CHOICES)
