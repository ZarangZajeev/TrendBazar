from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework import authentication, permissions
from rest_framework.decorators import action

from api.serializers import UserSerializer,ProductSerializer,BasketItemSerializer,BasketSeriliazer
from api.models import Product,BasketItem
# Create your views here.


class SiginUpView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

# url:http://127.0.0.1:8000/api/products/ 
class ProductView(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("Permission deneid")
    
    def update(self, request, *args, **kwargs):
        raise serializers.ValidationError("Permission deneid")
    
    def destroy(self, request, *args, **kwargs):
        raise serializers.ValidationError("Permission deneid")
    

    # url:http://127.0.0.1:8000/api/products/{id}/add_to_basket/
    @action(methods=["post"],detail=True)
    def add_to_basket(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        product_obj=Product.objects.get(id=id)
        basket_obj=request.user.cart
        serializer=BasketItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product_obj,basket=basket_obj)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
        

# url:http://127.0.0.1:8000/api/baskets/
class BasketView(viewsets.ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def list(self,request,*args,**kwargs):
        qs=request.user.cart
        serializer=BasketSeriliazer(qs,many=False)
        return Response(data=serializer.data)
    
class BasketItemView(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=BasketItemSerializer
    queryset=BasketItem.objects.all()

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("Permission Deneid")