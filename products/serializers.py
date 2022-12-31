from products.models import Product
from rest_framework import serializers


#serializing products
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

