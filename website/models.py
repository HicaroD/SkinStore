from django.utils.translation import gettext_lazy as _
from django.db import models

class Property(models.Model):
    class Properties(models.TextChoices):
        FACTORY_NEW    =  "FN", _("Factory New"),
        MINIMAL_WEAR   =  "MW", _("Minimal Wear"),
        FIELD_TESTED   =  "FT", _("Field Tested"),
        WELL_WORM      =  "WW", _("Well Worm"),
        BATTLE_SCARRED =  "BS", _("Battle Scarred"),

    name = models.CharField(
        max_length=25,
        choices=Properties.choices,
        default=Properties.FACTORY_NEW,
    )

    def __str__(self):
        return __str__

    class Meta:
        db_table = "property"

class Category(models.Model):
    class Categories(models.TextChoices):
        GLOVE  = "G", _('Glove'),
        PISTOL = "P", _('Pistol'),
        AWP    = "AW", _('AWP'),
        RIFLER = "R", _('Rifler'),
        KNIFE  = "K", _('Knife')

    name = models.CharField(
        max_length=25,
        choices=Categories.choices,
        default=Categories.KNIFE,
    )

    def __str__(self):
        return __str__

    class Meta:
        db_table = "category"


class Skin(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True)
    skin_property = models.ForeignKey(Property, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=19, decimal_places=4)
    primary_image_url = models.CharField(null=True, max_length=50)	
    secondary_image_url = models.CharField(null=True, max_length=50)

    def __str__(self):
	    return self.name

    class Meta:
        db_table = "skin"
        ordering = ["-price"]
