from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.viewsets import GenericViewSet
from .models import Item
from .serializers import ItemDetailSerializer, ItemSerializer


class ItemDetailViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
