from django.db import models
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
# Create your models here.
class Commodity(models.Model):
    commodityName = models.CharField( max_length = 50)
    exporterName = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.FloatField()
    quantityAvailable = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.commodityName
    def get_absolute_url(self):
        return f"/trade/mycommodities/{self.id}/"

class Trade(models.Model):
    tradeID = models.IntegerField()
    commodityName = models.CharField( max_length = 50)
    importerName = models.CharField( max_length = 50)
    exporterName = models.CharField( max_length = 50 )
    datePerformed = models.DateTimeField()
    totalPrice = models.FloatField()

    def __str__(self):
        return self.commodityName

# class CommodityRequested(models.Model):
#     commodityName = models.ForeignKey(commodityName)
