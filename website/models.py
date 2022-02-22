from django.utils.translation import gettext_lazy as _
from django.db import models

class Property(models.Model):
    class Properties(models.TextChoices):
        FACTORY_NEW    =  "Factory New", _("Factory New"),
        MINIMAL_WEAR   =  "Minimal Wear", _("Minimal Wear"),
        FIELD_TESTED   =  "Field Tested", _("Field Tested"),
        WELL_WORM      =  "Well Worm", _("Well Worm"),
        BATTLE_SCARRED =  "Battle Scarred", _("Battle Scarred"),

    name = models.CharField(
        max_length=25,
        choices=Properties.choices,
        default=Properties.FACTORY_NEW,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "property"

class Category(models.Model):
    class Categories(models.TextChoices):
        GLOVE  = "Glove", _('Glove'),
        PISTOL = "Pistol", _('Pistol'),
        AWP    = "AWP", _('AWP'),
        RIFLER = "Rifler", _('Rifler'),
        KNIFE  = "Knife", _('Knife')

    name = models.CharField(
        max_length=25,
        choices=Categories.choices,
        default=Categories.KNIFE,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"


class Skin(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True)
    skin_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=4)
    primary_image_url = models.URLField(null=True, max_length=200)	
    secondary_image_url = models.URLField(null=True, max_length=200)

    def __str__(self):
	    return self.name

    class Meta:
        db_table = "skin"
        ordering = ["-price"]
