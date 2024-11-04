import django
from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone
from branches.models import Branch


class Category(models.Model):

       
    CATEGORY_CHOICES = (
    ('LOTIONS', 'Lotions'),
    ('CREAMS', 'Creams'),
    ('CLOTHING', 'Clothing'),
    ('SHOES', 'Shoes'),
    ('COSMETICS', 'Cosmetics'),
    ('HAIR', 'Hair'),
    ('OTHER', 'Other'),
    )
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self) -> str:
        return self.name


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


#  carPart model
class Product(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField(max_length=255,)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    objects = ProductManager()

    def delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    def __str__(self) -> str:
        return self.name
   