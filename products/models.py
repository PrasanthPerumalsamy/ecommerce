from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=250)
    category_id   = models.PositiveBigIntegerField()

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category        = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title           = models.CharField(max_length=120)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image           = models.ImageField(null=True, blank=True)
    rating          = models.IntegerField(null=True, blank=True)
    active          = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProductType(models.Model):
    type_name       = models.CharField(max_length=250)
    type_id         = models.PositiveBigIntegerField()
    publications    = models.ManyToManyField(Product)

    def __str__(self):
        return self.type_name


class Review(models.Model):
   product          = models.ForeignKey(Product, on_delete=models.CASCADE)
   name             = models.CharField(max_length=200, null=True, blank=True)
   rating           = models.IntegerField(null=True, blank=True, default=0)
   comment          = models.TextField(null=True, blank=True)

   def __str__(self):
      return str(self.rating)