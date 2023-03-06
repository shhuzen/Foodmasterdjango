from django.db import models
from django.utils.timezone import now


# Create your models here.
class Items (models.Model):
    amount = models.IntegerField()
    name = models.CharField(max_length=100,unique=True)
    price = models.IntegerField()
    desc = models.CharField(max_length=250)
    image = models.ImageField(upload_to ='items/',default="none",null=True)
    def __str__(self):
        return self.name

class Cartloyal(models.Model):
    cartloyalid = models.CharField (verbose_name="Карта лояльности", max_length=20, default="")
    procent = models.IntegerField(null=True)

    def __str__(self):
        return str(self.cartloyalid)


class Orders(models.Model):
    mesto = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    products = models.ManyToManyField(Items)
    date_creation = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    date_last_update = models.DateTimeField(verbose_name="Последнее изменение", default=now)
    status = models.CharField(verbose_name="Статус", max_length=255, default="Не оплачен")
    check_info = models.FileField(verbose_name="Чек",upload_to="4ek/",null=True)
    cartloyal = models.ManyToManyField(Cartloyal)




    def __str__(self):
        return str(self.mesto)

