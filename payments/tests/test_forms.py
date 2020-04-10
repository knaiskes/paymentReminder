from django.test import TestCase
from payments.forms import DateHistorySearchForm

class DateHistorySearchFormTest(TestCase):
    def setUp(self):
        self.form = DateHistorySearchForm()

    def test_days_field_label(self):
        label = self.form.fields['days'].label == None or \
            self.form.fields['days'].label =='days'
        self.assertTrue(label)
