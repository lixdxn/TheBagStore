from django.urls import path
from . import views
from .views import AddProductAPI, CategoryListView, ProductDetailAPI

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('category/<int:category_id>', views.category_products, name='category_products'),
    path('api/add-product/', AddProductAPI.as_view(), name='add_product_api'),
    path('api/categories/', CategoryListView.as_view(), name='category_list_api'),
    path('api/products/', views.ProductListView.as_view(), name='product_list_api'),
    path('api/products/<int:pk>/', ProductDetailAPI.as_view(), name='product_detail_api'),

]