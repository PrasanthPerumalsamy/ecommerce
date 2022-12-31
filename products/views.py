from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Product
from .serializers import ProductSerializer
# Create your views here.


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    name = 'product-list'

    filterset_fields = ['category', 'active']
    search_fields = ['title', 'category__category_name']
    ordering_fields = ['id', 'price', 'category']
