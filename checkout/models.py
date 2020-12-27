from django.db import models

from listings.models import Listing
from django.contrib.auth.models import User


# Create your models here.
class Purchase(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(blank=False)
    qty = models.IntegerField(blank=False)

    def __str__(self):
        return f"Purchase for listing#{self.listing.id} by user#{self.user.id}"
