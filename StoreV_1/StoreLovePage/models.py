from django.db import models
import os


# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=30)

class ShopItems(models.Model):
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=30)
	price = models.IntegerField()
	currency = models.CharField(max_length=30)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	icon = models.ImageField(upload_to='images/')


class PictareForShop(models.Model):
	shopitems = models.ForeignKey(ShopItems, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to='images/')


	
