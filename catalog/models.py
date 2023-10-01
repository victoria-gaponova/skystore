from django.db import models


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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', blank=True, null=True)
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
