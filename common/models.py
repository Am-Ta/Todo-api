from django.db import models


class BaseModel(models.Model):
    """ Base Model to Inherit The All Models """

    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modify_data = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
