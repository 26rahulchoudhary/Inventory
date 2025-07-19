from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View
from .models import Product
from .serializers import ProductSerializer
from django import forms

# Product CRUD: List, Create, Retrieve, Update, Delete
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Adjust stock (increase or decrease quantity)
class AdjustStockView(APIView):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        amount = request.data.get('amount')
        if amount is None:
            return Response({'error': 'Amount is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            amount = int(amount)
        except ValueError:
            return Response({'error': 'Amount must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
        product.quantity_in_stock += amount
        if product.quantity_in_stock < 0:
            return Response({'error': 'Stock cannot be negative.'}, status=status.HTTP_400_BAD_REQUEST)
        product.save()
        return Response(ProductSerializer(product).data)

# List products below a stock threshold
class LowStockListView(APIView):
    def get(self, request):
        threshold = request.query_params.get('threshold', 10)
        try:
            threshold = int(threshold)
        except ValueError:
            threshold = 10
        low_stock_products = Product.objects.filter(quantity_in_stock__lt=threshold)
        serializer = ProductSerializer(low_stock_products, many=True)
        return Response(serializer.data)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'category', 'price', 'quantity_in_stock']

class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'inventory/product_list.html', {'products': products})

class ProductAddView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'inventory/product_form.html', {'form': form})
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        return render(request, 'inventory/product_form.html', {'form': form})

class ProductEditView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'inventory/product_form.html', {'form': form})
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
        return render(request, 'inventory/product_form.html', {'form': form})

class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('product-list')

class AdjustStockHtmlView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'inventory/adjust_stock.html', {'product': product})
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        try:
            amount = int(request.POST.get('amount'))
        except (TypeError, ValueError):
            amount = 0
        product.quantity_in_stock += amount
        if product.quantity_in_stock < 0:
            product.quantity_in_stock = 0
        product.save()
        return redirect('product-list')
