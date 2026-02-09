from django.db import models
from django.conf import settings

CURRENCY_CHOICES = [
    ("CAD", "Canadian Dollar"),
    ("USD", "US Dollar"),
    ("BRL", "Brazilian Real"),
]
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    default_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="CAD")
    
    def __str__(self):
        return f'{self.user.username}\'s Profile'