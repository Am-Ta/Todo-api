from rest_framework import serializers
from item.models import Item
from category.serializers import CategorySerializer
from user.serializers import UserDetailSerializer
from datetime import datetime


class ItemDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = UserDetailSerializer()
    created_date = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['id', 'title', 'description',
                  'category', 'user', 'created_date']

    def get_created_date(self, obj):
        return datetime.strftime(obj.created_date, "%b %d %Y %H:%M:%S")


class ItemSerializer(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['title', 'user', 'category', 'created_date']

    def get_created_date(self, obj):
        return datetime.strftime(obj.created_date, "%b %d %Y %H:%M:%S")
