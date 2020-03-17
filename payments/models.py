from django.db import models

class Obliged(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=130, unique=True)

    def __str__(self):
        return self.full_name
