from django import forms

DAYS_CHOICES = (
    ('', '-----'),
    ('seven', '7 Days'),
    ('thirty', '30 Days'),
    ('sixty', '60 Days'),
    ('ninety', '90 days'),
)

class DateHistorySearchForm(forms.Form):
    days = forms.ChoiceField(choices = DAYS_CHOICES)
