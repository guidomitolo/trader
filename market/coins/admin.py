from django.contrib import admin
from .models import Coin, Currency, History


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "code",
    ]
    list_display = [
        "name",
        "code",
    ]


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "code",
    ]
    list_display = [
        "name",
        "code",
    ]


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    fields = [
        "coin",
        "currency",
        "timestamp",
        "price",
        "market_cap",
        "total_volume",
    ]
    list_display = [
        "coin",
        "currency",
        "timestamp",
        "price",
        "market_cap",
        "total_volume",
    ]