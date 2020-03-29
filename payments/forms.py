from django import forms

DAYS_CHOICES = (
    ('', '-----'),
    ('seven', '7 Days'),
    ('thirty', '30 Days'),
    ('sixty', '60 Days'),
    ('ninety', '90 days'),
)

class DateHistorySearchForm(forms.Form):
    days = forms.ChoiceField(help_text="Select days: ",choices = DAYS_CHOICES)
