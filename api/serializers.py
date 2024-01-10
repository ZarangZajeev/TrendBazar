from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Product,Basket,BasketItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        read_only_fields=["id","category"]

    category=serializers.StringRelatedField()

class BasketItemSerializer(serializers.ModelSerializer):
    product=serializers.StringRelatedField()
    class Meta:
        model=BasketItem
        fields="__all__"
        read_only_fields=[
                            "id",
                            "product",
                            "basket",
                            "is_active",
                            "created_at",
                            "updated_at",
                            "total"
                        ]
