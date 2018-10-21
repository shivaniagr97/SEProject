from django.db import models

# Create your models here.
class Commodity(models.Model):
    commodityName = models.CharField( max_length = 50, help_text = 'Enter name of commodity')
    exporterName = models.CharField( max_length = 50)
    price = models.FloatField()
    quantityAvailable = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.commodityName + " " + self.exporterName

class Trade(models.Model):
    tradeID = models.IntegerField()
    commodityName = models.CharField( max_length = 50)
    importerName = models.CharField( max_length = 50)
    exporterName = models.CharField( max_length = 50 )
    datePerformed = models.DateTimeField()
    totalPrice = models.FloatField()

    def __str__(self):
        return self.commodityName
