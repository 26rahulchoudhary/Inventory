from django.urls import path
from .views import (
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    AdjustStockView,
    LowStockListView,
    ProductListView,
    ProductAddView,
    ProductEditView,
    ProductDeleteView,
    AdjustStockHtmlView,
)

urlpatterns = [
    # HTML views
    path('', ProductListView.as_view(), name='product-list'),
    path('add/', ProductAddView.as_view(), name='product-add'),
    path('edit/<int:pk>/', ProductEditView.as_view(), name='product-edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('adjust-stock/<int:pk>/', AdjustStockHtmlView.as_view(), name='product-adjust-stock'),

    # API endpoints
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('products/<int:pk>/adjust-stock/', AdjustStockView.as_view(), name='adjust-stock'),
    path('low-stock/', LowStockListView.as_view(), name='low-stock'),
] 