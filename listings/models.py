from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return f"{self.category_name}"


class Listing(models.Model):
    # fields / attributes of this table
    title = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(blank=False)
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cover = CloudinaryField()


    # toString function -- allow us to state the string rep of class
    def __str__(self):
        return self.title


class Brand(models.Model):
    # the fields (i.e. attributes of table)
    name = models.CharField(blank=False, max_length=100)
    website = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return f"{self.name} ({self.website})"


class Seller(models.Model):
    seller_name = models.CharField(blank=False, max_length=255)
    seller_email = models.CharField(blank=False, max_length=255)
    seller_contact = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return f"{self.seller_name} ({self.seller_email})"
