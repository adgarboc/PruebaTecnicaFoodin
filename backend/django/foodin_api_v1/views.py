from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from foodin_api_v1.models import Product
from foodin_api_v1.serializers import ProductModelSerializer


class ProductAPIView(APIView):
    parser_classes = (JSONParser, )
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk: int = None):
        if pk:
            products = Product.objects.filter(pk=pk)
        else:
            products = Product.objects.all()
        if not products:
            return Response(status=404)
        data = ProductModelSerializer(products, many=True).data
        return Response(data)

    def post(self, request):
        serializer = ProductModelSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk: int = None):
        if not pk:
            return Response(status=400)
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        serializer = ProductModelSerializer(product, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk: int = None):
        if not pk:
            return Response(status=400)
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        product.delete()
        return Response(status=204)


""" 

Otra forma de hacerlo

@api_view(['GET'])
def product_get(request, pk: int = None):
    if pk:
        products = Product.objects.filter(pk=pk)
    else:
        products = Product.objects.all()
    if not products:
        return Response(status=404)
    data = ProductModelSerializer(products, many=True).data
    return Response(data)


@api_view(['POST'])
def product_post(request):
    serializer = ProductModelSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def product_put(request, pk: int = None):
    if not pk:
        return Response(status=400)
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductModelSerializer(product, data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def product_delete(request, pk: int = None):
    if not pk:
        return Response(status=400)
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=404)
    product.delete()
    return Response(status=204)


"""
