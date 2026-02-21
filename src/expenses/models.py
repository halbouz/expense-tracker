from django.db import models
from django.conf import settings


class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="expenses")
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.PROTECT,
        related_name="expenses",
    )
    
    description = models.CharField(max_length=255,blank=True,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.user} - {self.amount} on {self.date}"