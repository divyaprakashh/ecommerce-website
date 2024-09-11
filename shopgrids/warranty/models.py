# warranty/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone
from productmanagement.models import Products  # Assuming the correct singular form 'Product'
from useraccount.models import Accounts  # Adjust import based on your actual User Profile model
from cart.models import Order



from productmanagement.models import Products
from useraccount.models import Accounts
from django.utils import timezone

class Warranty(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def is_valid(self):
        today = timezone.now().date()
        return self.start_date <= today <= self.end_date

    def __str__(self):
        return f"Warranty for {self.product.name} (owned by {self.user.username}) from {self.start_date} to {self.end_date}"
