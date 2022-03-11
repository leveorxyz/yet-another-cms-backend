from django.db import models
from core.models import CoreModel
from user.models import User

# Create your models here.

class Category(CoreModel):
    title = models.CharField(max_length=100,default="",blank=False,null=False)
    thumbnail = models.CharField(max_length=255, default=None, blank=True, null=True)
    image_alt = models.CharField(max_length=255, default=None, null=True, blank=True)

class Product(CoreModel):
    title = models.CharField(max_length=100, default="", null=False, blank=False)
    price = models.FloatField(default=0.0)
    thumbnail = models.CharField(max_length=100, default=None, blank=True, null=True)
    image_alt = models.CharField(max_length=100, default=None, null=True, blank=True)
    is_trending = models.BooleanField(default=False, blank=True)
    stock = models.PositiveIntegerField(default=0, blank=True)
    tags = models.CharField(max_length=4096, default="", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    description = models.CharField(max_length=500, null=True, blank=True, default=None)

