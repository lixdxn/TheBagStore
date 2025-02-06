from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


def home(request):
    """Главная страница с категориями и товарами в них"""
    categories = Category.objects.prefetch_related('product_set')
    return render(request, 'catalog/home.html', {'categories': categories})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'catalog/categories.html', {'categories': categories})

def product_detail(request, product_id):
    """Отображает страницу конкретного товара"""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})

def category_products(request, category_id):
    """Отображает товары внутри выбранной категории."""
    category = get_object_or_404(Category, id=category_id)
    products = category.product_set.all()
    return render(request, 'catalog/category_products.html', {'category': category, 'products': products})

class ProductListAPI(APIView):
    """Получение списка товаров и добавление нового товара."""
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPI(APIView):
    """Получение, обновление и удаление конкретного товара."""
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def patch(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class CategoryListAPI(APIView):
    """Получение списка категорий и добавление новой категории."""
    def get(self, request):
        categories = Category.objects.values('id', 'name', 'description')
        return Response({'categories': list(categories)}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
