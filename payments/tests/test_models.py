from django.test import TestCase
from payments.models import Obliged

class ObligedModelTest(TestCase):
    def test_str_representation(self):
        obliged = Obliged(full_name='Example Name', email='ExampleName@example.com')
        self.assertEqual(str(obliged), obliged.full_name)
