from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemDetailViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'detail', ItemDetailViewSet)
router.register(r'todo', ItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
