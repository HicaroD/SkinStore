from django.db import models
from SkinStore.website.models.Skin

class Cart(models.Model):
    items = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    total_amount = models.DecimalField()

class CartItem(models.Model):
    product = models.OneToOneField(
        Skin, 
        on_delete=models.CASCADE,
        primary_key=True
    )
    quantity = PositiveIntegerField()
