from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .serializers import *
from home_app.models import*
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import*
 
def test_api_view(request):
    first_combo = Combo.objects.first()
    f_c = {'name':first_combo.name}
    return JsonResponse(f_c)

@api_view(['GET', 'POST', 'PUT'])
def combo_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data = ComboSerializer(instance = Combo.objects.all(), many = True).data, status=200)
        else:
            current_combo = get_object_or_404(Combo, pk=pk)
            return Response(data = ComboSerializer(instance = current_combo).data, status=200)
    elif request.method == 'POST':
        sc = ComboSerializer(data=request.data)
        if sc.is_valid():
            sc.save()
            return Response({'id':sc.instance.id}, status=201)
        else:
            return Response(sc.error_messages, status = 406)
    elif request.method == 'PUT':
        current_combo = get_object_or_404(Combo, pk = pk)
        sc = ComboSerializer(data=request.data, instance = current_combo)
        if sc.is_valid():
            sc.save()
            return Response('Updated', status=200)
        else:
            return Response(sc.error_messages, status=406)
    else:
        current_combo = get_object_or_404(Combo, pk = pk)
        current_combo.delete()

class ComboListview(ListAPIView):
    queryset = Combo.objects.all() 
    serializer_class = ComboSerializer

class ComboCreate(CreateAPIView):
    queryset = Combo.objects.all() 
    serializer_class = ComboSerializer 

class ComboUpdate(UpdateAPIView):
    queryset = Combo.objects.all() 
    serializer_class = ComboSerializer 
    lookup_field = 'pk'

class ComboDelete(DestroyAPIView):
    queryset = Combo.objects.all() 
    serializer_class = ComboSerializer 
    lookup_field = 'pk'

class ProductListview(ListAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer

class ProductCreate(CreateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 

class ProductUpdate(UpdateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    lookup_field = 'pk'

class ProductDelete(DestroyAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    lookup_field = 'pk'

class ResursListview(ListAPIView):
    queryset = Resurs.objects.all() 
    serializer_class = ResursSerializer

class ResursCreate(CreateAPIView):
    queryset = Resurs.objects.all() 
    serializer_class = ResursSerializer 

class ResursUpdate(UpdateAPIView):
    queryset = Resurs.objects.all() 
    serializer_class = ResursSerializer 
    lookup_field = 'pk'

class ResursDelete(DestroyAPIView):
    queryset = Resurs.objects.all() 
    serializer_class = ResursSerializer 
    lookup_field = 'pk'

class Fast_food_Listview(ListAPIView):
    queryset = Fast_food_branch.objects.all() 
    serializer_class = Fast_food_Serializer

class Fast_food_Create(CreateAPIView):
    queryset = Fast_food_branch.objects.all() 
    serializer_class = Fast_food_Serializer 

class Fast_food_Update(UpdateAPIView):
    queryset = Fast_food_branch.objects.all() 
    serializer_class = Fast_food_Serializer 
    lookup_field = 'pk'

class Fast_food_Delete(DestroyAPIView):
    queryset = Fast_food_branch.objects.all() 
    serializer_class = Fast_food_Serializer 
    lookup_field = 'pk'

class OrdersListview(ListAPIView):
    queryset = Orders.objects.all() 
    serializer_class = OrdersSerializer

class OrdersCreate(CreateAPIView):
    queryset = Orders.objects.all() 
    serializer_class = OrdersSerializer 

class OrdersUpdate(UpdateAPIView):
    queryset = Orders.objects.all() 
    serializer_class = OrdersSerializer 
    lookup_field = 'pk'

class OrdersDelete(DestroyAPIView):
    queryset = Orders.objects.all() 
    serializer_class = OrdersSerializer 
    lookup_field = 'pk'
    