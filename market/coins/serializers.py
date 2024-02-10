from rest_framework import serializers
from .models import History, Coin


class HistorySerializer(serializers.ModelSerializer):
    currency = serializers.SerializerMethodField("get_currency")

    def get_currency(self, obj):
        return obj.currency.code

    class Meta:
        model = History
        fields = [
            "timestamp",
            "coin",
            "currency",
            "price",
            "market_cap",
            "total_volume",
        ]
        lookup_field = "coin"


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = "__all__"