from django.contrib import admin

# Register your models here.

from products.models import ProductCategory, Product, Review, ProductType


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "rating")

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ProductType)