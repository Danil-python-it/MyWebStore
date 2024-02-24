from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	avatars = models.ImageField(upload_to='avatars/', blank=True)


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


class Baskets(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	shopitems = models.ForeignKey(ShopItems, on_delete=models.CASCADE)
