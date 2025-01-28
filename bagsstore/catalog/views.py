from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer


def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})

def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Category.products.all()
    return render(request, 'catalog/category_products.html', {'category': category})


class AddProductAPI(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(View):
    def get(self, request):
        categories = list(Category.objects.values('id', 'name', 'description'))
        return JsonResponse({'categories': categories}, safe=False)