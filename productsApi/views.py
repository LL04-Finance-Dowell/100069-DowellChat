from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Products
from .serializers import ProductsSerializer
from rest_framework import status


class ProductsViewSet(viewsets.ViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def list(self, request):
        products = self.queryset
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            json_data = serializer.data
            # print(json_data)
            name = json_data.get('name', None)
            message = {
                'message': f'{name} created successfully',
                'data': json_data
            }
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            products = Products.objects.get(id=id)
            serializer = ProductsSerializer(products)
            return Response(serializer.data)
        return Response({'message': 'id is required'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        if id is not None:
            product = Products.objects.get(id=id)
            serializer = ProductsSerializer(
                instance=product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                json_data = serializer.data
                name = json_data.get('name', None)
                message = {
                    'message': f'{name} updated successfully',
                    'data': json_data
                }
                return Response(message, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'id is required'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        id = pk
        if id is not None:
            product = Products.objects.get(id=id)
            product.delete()
            message = {
                'message': 'Product deleted successfully',
                'data': {}
            }
            return Response(message, status=status.HTTP_201_CREATED)
        return Response({'message': 'id is required'}, status=status.HTTP_400_BAD_REQUEST)
