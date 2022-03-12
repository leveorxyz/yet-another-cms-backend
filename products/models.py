from django.db import models
from core.models import CoreModel
from user.models import User

# Create your models here.

#Category Class : Inherits from CoreModel 
class Category(CoreModel):
    title = models.CharField(max_length=100,default="",blank=False,null=False) #Title of the category
    thumbnail = models.CharField(max_length=255, default=None, blank=True, null=True) #Thumbnail of the category
    image_alt = models.CharField(max_length=255, default=None, null=True, blank=True) #Alternative text incase the thumbnail fails

#Tag Class : Inherits from CoreModel
class Tag(CoreModel):
    title = models.CharField(max_length=255) #Title of the tag

#Product Class : Inherits from CoreModel
class Product(CoreModel):
    title = models.CharField(max_length=100, default="", null=False, blank=False) #Title of the product
    price = models.FloatField(default=0.0) #Price of the product
    thumbnail = models.CharField(max_length=100, default=None, blank=True, null=True) #Thumbnail of the product
    image_alt = models.CharField(max_length=100, default=None, null=True, blank=True) #Alternative text incase the thumbnail fails
    is_trending = models.BooleanField(default=False, blank=True) #Is the product trending
    stock = models.PositiveIntegerField(default=0, blank=True) #Quantity of the product in stock
    tag = models.ManyToManyField(Tag,on_delete = models.SET_NULL, blank=True,null=True,related_name="tags") #related tags of each product
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    ) #related category of each product
    description = models.CharField(max_length=500, null=True, blank=True, default=None) #Description of the product

#Product Image Class : Inherits from CoreModel
class ProductPhoto(CoreModel):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    ) #related product of each product image (Foreign Key)
    url = models.CharField(max_length=255, default=None, blank=True, null=True) #URL of the product image
