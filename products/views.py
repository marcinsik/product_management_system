
from rest_framework.response import Response
from rest_framework.views import APIView

from products.serializers import ProductListSerializer,WarehouseListSerializer,ProductDetailSerializer,\
    AddProductSerializer,AddWarehouseSerializer

from products.models import Product,Warehouse

# Create your views here.
class WarehouseView(APIView):
    def get(self, request):
        warehouses= Warehouse.objects.all()
        warehouse_serializer = WarehouseListSerializer(warehouses, many=True)
        return Response(warehouse_serializer.data)



    def post(self,request):
        data = request.data
        serializer = AddWarehouseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WarehouseDetailView(APIView):
    def delete(self, request, warehouse_id):
        try:
            warehouse = Warehouse.objects.get(pk=warehouse_id)
            warehouse.delete()
            return Response({'status': 'success', 'message': 'Warehouse deleted '})
        except Warehouse.DoesNotExist:
            return Response({'status': 'failure', 'message': 'Warehouse does not exist '})

    def get(self,request,warehouse_id):
        warehouse = Warehouse.objects.get(pk=warehouse_id)
        warehouse_serializer = WarehouseListSerializer(warehouse)
        return Response(warehouse_serializer.data)


class ProductView(APIView):
    def get(self, request):
        name = request.GET.get('name', None)
        products = Product.objects.all()

        if name is not None:
            products = products.filter(name__icontains=name)
        product_Serializer = ProductListSerializer(products, many=True)
        return Response(product_Serializer.data)

    def post(self, request):
        try:
            data = request.data
            serializer = AddProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'status': 'failure', 'error': serializer.errors})
        except Exception as e:
            return Response({'status': 'failure', 'error': 'error'})

class ProductDetailView(APIView):
    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        return Response(ProductDetailSerializer(product).data)

    def delete(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
            product.delete()
            return Response({'status': 'success', 'message': 'product deleted !'})
        except Product.DoesNotExist:
            return Response({'status': 'failure', 'message': 'prodoct  not available!'})

    def put(self, request, product_id):
        data = request.data
        product = Product.objects.get(pk=product_id)
        serializer = AddProductSerializer(product, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'status': 'failure', 'error': serializer.errors})
