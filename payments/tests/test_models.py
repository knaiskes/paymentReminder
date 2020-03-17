from django.test import TestCase
from payments.models import Obliged, Payment

class ObligedModelTest(TestCase):
    def test_str_representation(self):
        obliged = Obliged(full_name='Example Name', email='ExampleName@example.com')
        self.assertEqual(str(obliged), obliged.full_name)


class PaymentModelTest(TestCase):
    def test_str_representation(self):
        obliged = Obliged(full_name='Example Name', email='ExampleName@example.com')
        payment = Payment(name='Example_Name', payment_code='100-200-300',
                          description='This is a test', amount=20.33, obliged=obliged)
        self.assertEqual(str(payment), payment.name)
