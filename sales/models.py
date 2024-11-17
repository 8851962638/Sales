from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    referral_fee = models.FloatField()
    total_cost = models.FloatField()

    def __str__(self):
        return self.name
