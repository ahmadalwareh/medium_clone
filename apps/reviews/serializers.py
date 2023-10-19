from .models import Product, Category
from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'category']


class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User

    @staticmethod
    def get_days_since_joined(obj):
        return (now() - obj.date_joined).days
