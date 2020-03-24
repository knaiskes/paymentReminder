from django.db import models
from django.urls import reverse

class Obliged(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=130, unique=True)

    def get_obliged_url(self):
        return reverse('payments:obliged_by_id', args=[self.id])

    def __str__(self):
        return self.full_name

class Payment(models.Model):
    name = models.CharField(max_length=50, unique=True)
    payment_code = models.CharField(max_length=80)
    description = models.TextField(max_length=150, blank=True)
    amount = models.FloatField()
    obliged = models.ForeignKey(Obliged, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name
