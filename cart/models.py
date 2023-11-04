# Create your models here.
from django.db import models
from django.contrib.sessions.models import Session  # Import the Session model
from django.contrib.auth import get_user_model

from my_pharmacy.models import Products

CustomUser = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user or 'Guest'}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, related_name='cart_items')
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name}"

    def sub_total(self):
        return self.product.product_price * self.quantity
