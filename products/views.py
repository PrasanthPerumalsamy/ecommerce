from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework as filters_custom

from .models import Product, ProductType
from .serializers import ProductSerializer
# Create your views here.

class MyFilterSet(filters_custom.FilterSet):
    producttype = filters_custom.ModelMultipleChoiceFilter(queryset=ProductType.objects.all())

    class Meta:
        model = Product
        fields = ['producttype', 'category', 'active']

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    name = 'product-list'

    search_fields = ['title', 'category__category_name']
    ordering_fields = ['id', 'price', 'category', 'rating']
    filterset_class = MyFilterSet