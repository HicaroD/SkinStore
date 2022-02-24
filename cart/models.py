from django.db import models

from website.models import Skin

class CartItem(models.Model):
    product = models.OneToOneField(
        Skin, 
        on_delete=models.CASCADE,
        primary_key=True
    )
    quantity = PositiveIntegerField()
