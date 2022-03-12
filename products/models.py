from django.db import models
from django.conf import settings
from core.models import CoreModel
from core.literals import *
from core.utils import *

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
    _thumbnail = models.ImageField(
        upload_to=PRODUCT_THUMBNAIL_DIRECTORY,
        blank = True,
        null = True,
    ) #Thumbnail of the product
    image_alt = models.CharField(max_length=100, default=None, null=True, blank=True) #Alternative text incase the thumbnail fails
    is_trending = models.BooleanField(default=False, blank=True) #Is the product trending
    stock = models.PositiveIntegerField(default=0, blank=True) #Quantity of the product in stock
    tag = models.ManyToManyField(Tag,on_delete = models.SET_NULL, blank=True,null=True,related_name="tags") #related tags of each product
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, default=None
    ) #related category of each product
    description = models.CharField(max_length=500, null=True, blank=True, default=None) #Description of the product

    #getter for product thumbnail

    @property
    def thumbnail(self) -> str:
        return  settings.MEDIA_URL + self.thumbnail.name
    
    @thumbnail.setter
    def thumbnail(self, value: str):
        if self._thumbnail.name:
            del self.thumbnail
        file_name, file = generate_file_and_name(value, self.id)
        self._thumbnail.save(file_name, file, save=True)
        self.save()
    
    @thumbnail.deleter
    def thumbnail(self):
        if self._thumbnail.name:
            self._thumbnail.delete(save=True)
    
    def delete(self, *args, **kwargs):
        del self.thumbnail
        return super(Product, self).delete(*args, **kwargs)





#Product Image Class : Inherits from CoreModel
class ProductDetailPhoto(CoreModel):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    ) #related product of each product image (Foreign Key)
    url = models.CharField(max_length=255, default=None, blank=True, null=True) #URL of the product image
