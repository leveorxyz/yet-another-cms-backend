from django.db import models
from core.models import CoreModel
from user.models import User

# Create your models here.

class Category(CoreModel):
    title = models.CharField(max_length=100,default="",blank=False,null=False)
    thumbnail = models.CharField(max_length=255, default=None, blank=True, null=True)
    image_alt = models.CharField(max_length=255, default=None, null=True, blank=True)




