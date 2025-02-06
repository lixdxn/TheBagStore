from django.urls import path
from . import views
from .views import ProductListAPI, CategoryListAPI, ProductDetailAPI


urlpatterns = [
    path('', views.home, name='home'),
    path('categories/product/<int:product_id>', views.product_detail, name='product_detail'),
    path('category/<int:category_id>', views.category_products, name='category_products'),
    path('categories/', views.categories, name='categories'),

    path('api/categories/', CategoryListAPI.as_view(), name='category_list_api'),
    path('api/products/', ProductListAPI.as_view(), name='product_list_api'),
    path('api/products/<int:pk>/', ProductDetailAPI.as_view(), name='product_detail_api'),

]