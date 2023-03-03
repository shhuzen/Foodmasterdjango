from django.db import models

# Create your models here.
class Items (models.Model):
    amount = models.IntegerField()
    name = models.CharField(max_length=100,unique=True)
    price = models.IntegerField()
    desc = models.CharField(max_length=250)
    image = models.ImageField(upload_to ='items/',default="none")
    def __str__(self):
        return self.name


class Orders (models.Model):
    price = models.IntegerField()
    products = models.ManyToManyField(Items)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.desc