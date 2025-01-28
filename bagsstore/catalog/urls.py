from django.urls import path
from . import views
from .views import AddProductAPI, CategoryListView

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>', views.product_detail, name='product_detail'),
    path('category/<int:category_id>', views.category_products, name='category_products'),
    path('api/add-product/', AddProductAPI.as_view(), name='add_product_api'),
    path('api/categories/', CategoryListView.as_view(), name='category_list_api'),  # ✅ Добавили маршрут

]