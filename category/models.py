from django.db import models
from common.models import BaseModel
from .base_categories import categories


class Category(BaseModel):
    category_name = models.CharField(max_length=100, choices=categories, unique=True)
