from rest_framework import serializers
from .models import User
from datetime import datetime


class UserDetailSerializer(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['name', 'user_name', 'email',
                  'age', 'description', 'created_date']

    def get_created_date(self, obj):
        return datetime.strftime(obj.created_date, "%b %d %Y %H:%M:%S")
