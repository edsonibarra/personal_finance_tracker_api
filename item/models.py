from django.db import models


class Item(models.Model):
    class PaymentType(models.TextChoices):
        cash = "cash", "Cash"
        debit_card = "DC", "Debit Card"
        credit_card = "CC", "Credit Card"

    title = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    pymnt = models.CharField(max_length=4, choices=PaymentType.choices)

    def __str__(self):
        return f"{self.title}, {self.amount}, {self.pymnt}"
    