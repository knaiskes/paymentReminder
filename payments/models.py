from django.db import models

class Obliged(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=130, unique=True)

    def __str__(self):
        return self.full_name

class Payment(models.Model):
    name = models.CharField(max_length=50, unique=True)
    payment_code = models.CharField(max_length=80)
    description = models.TextField(max_length=150, blank=True)
    amount = models.FloatField()
    obliged = models.ForeignKey(Obliged, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
