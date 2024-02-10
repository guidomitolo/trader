from django.db import models
from django.db.models import Q

class Currency(models.Model):
    code = models.CharField(max_length=8, verbose_name='Code', unique=True)
    name = models.CharField(max_length=16, verbose_name='Name')
        
    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'
        db_table = 'coin_currency'
        app_label = 'coins'

    def __str__(self) -> str:
        return f"{self.name}"


class Coin(models.Model):
    code = models.CharField(max_length=64, verbose_name='Code', unique=True)
    name = models.CharField(max_length=128, verbose_name='Name')
        
    class Meta:
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'
        db_table = 'coins_coin'
        app_label = 'coins'

    def __str__(self) -> str:
        return f"{self.name}"
    

class History(models.Model):
    timestamp = models.DateTimeField(unique_for_date="timestamp")
    coin = models.ForeignKey(Coin, verbose_name="Coin", on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, verbose_name="Currency", on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Price")
    market_cap = models.FloatField(verbose_name="Market Cap")
    total_volume = models.FloatField(verbose_name="Total Volume")

    class Meta:
        verbose_name = 'History'
        verbose_name_plural = 'History'
        db_table = 'coins_history'
        app_label = 'coins'
        

    def __str__(self) -> str:
        return f"{self.coin.name}: {self.timestamp} - {self.currency.code} {self.price}"