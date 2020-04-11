from django.test import TestCase
from payments.forms import DateSearchForm

class DateSearchFormTest(TestCase):
    def setUp(self):
        self.form = DateSearchForm()

    def test_days_field_label(self):
        label = self.form.fields['days'].label == None or \
            self.form.fields['days'].label =='Date range'
        self.assertTrue(label)

    def test_obligeds_field_label(self):
        label = self.form.fields['obligeds'].label == None or \
            self.form.fields['obligeds'].label == 'Select obliged'
        self.assertTrue(label)
