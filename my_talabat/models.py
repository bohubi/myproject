from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    number = models.IntegerField()

    def __str__(self):
        return self.name


class MenuCategory(models.Model):
    res = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    cat = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ing = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name
