from django.db import models
from common.models import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=40, unique=True)
    age = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
