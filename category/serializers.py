from rest_framework import serializers
from .models import Category
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['created_date', 'category_name']

    def get_created_date(self, obj):
        return datetime.strftime(obj.created_date, "%b %d %Y %H:%M:%S")
