from django.db import models
from django.db.models import Q

from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    class Meta:
        ordering = ("-created_at",)

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products_images', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Product(pk={self.pk}, name={self.name!r})"

    def get_preview(self):
        return self.description.split('-')[1:]


class Contact(models.Model):
    country = models.CharField(max_length=100)
    inn = models.CharField(max_length=18)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country} {self.address}"


class Version(models.Model):
    products = models.ManyToManyField(Product, related_name='versions', blank=True)
    number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return self.name
