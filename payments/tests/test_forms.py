from django.test import TestCase
from payments.forms import DateHistorySearchForm

class DateHistorySearchFormTest(TestCase):
    def setUp(self):
        self.form = DateHistorySearchForm()

    def test_days_field_label(self):
        label = self.form.fields['days'].label == None or \
            self.form.fields['days'].label =='days'
        self.assertTrue(label)

    def test_days_field_help_text(self):
        help_text = 'Select days: '
        self.assertEqual(self.form.fields['days'].help_text, help_text)
