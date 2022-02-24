from django.db import models

from website.models import Skin

class CartItem(models.Model):
    product = models.OneToOneField(
        Skin, 
        on_delete=models.CASCADE,
        primary_key=True
    )
    quantity = models.PositiveIntegerField()

class Cart(models.Model):
    items = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=19, decimal_places=4)

