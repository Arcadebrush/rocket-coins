from django.db import models

# Create your models here.
class Coins(models.Model):
    Coin_name = models.CharField(max_length=40)
    Symbol = models.CharField(max_length=10)
    #add image later
    Forked_from = models.CharField(max_length=30)
    Minable = models.CharField(max_length=5)
    Type = models.CharField(max_length=30)
    Token_type = models.CharField(max_length=20)
    ICO = models.CharField(max_length=10)
    Hashing_algorithm = models.CharField(max_length=30)
    Consensus_algorithm = models.CharField(max_length=50)
    Whitepaper = models.CharField(max_length=1000)
    Block_time = models.CharField(max_length=50)
    Founder = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    MarketCap = models.IntegerField(default=0)
    Volume_24 = models.IntegerField(default=0)

    def __str__(self):
        return self.Coin_name + " - " + self.Symbol
