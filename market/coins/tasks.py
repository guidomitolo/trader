from datetime import datetime, timedelta
import time
from .models import Currency, Coin, History
from django.conf import settings
import requests
import json
from tqdm import tqdm
import pytz
from celery import shared_task
from django.db import transaction
from django.db import connection


from celery.utils.log import get_task_logger


@shared_task
def update_coin_history(coin, currency, until):
    logger = get_task_logger(__name__)
    try:
        with connection.cursor() as cursor:
            with transaction.atomic():
                logger.info(f"Coin's History import starting")
                api_connection = CoinGeckoApiConnection(coin, currency)
                api_connection.save_updated_coin_data(from_override=until)
                print("Import successfull")
    except Exception as error:
        print(error)
        print("Import failed")


class CoinGeckoApiConnection():
      
    def __init__(self, coin_code, currency_code) -> None:
        self.coin_code = coin_code
        self.currency_code = currency_code

    def save_updated_coin_data(self, from_override=None):

        now = datetime.now()
        until_date = time.mktime(now.timetuple())
        from_date = time.mktime((now - timedelta(days=90)).timetuple())

        if from_override: from_date = time.mktime(from_override.timetuple())

        api_endpoint = f"{settings.API_COINGECKO}{self.coin_code}{settings.API_COINGECKO_HISTORY_ENDPOINT}"
        api_params = f"vs_currency={self.currency_code}&from={from_date}&to={until_date}&precision=2"
        full_api_endpoint = api_endpoint + api_params

        response = requests.get(full_api_endpoint)
        data = json.loads(response.content)

        currency = Currency.objects.get(code=self.currency_code)
        coin = Coin.objects.get(code=self.coin_code)

        history = self.parse_data(data, coin, currency)
        self.save_coin_history(history)

    def parse_data(self, data, coin, currency):
        coin_history = []
        for i in range(len(data["prices"])):
            coin_history.append({
                "coin": coin,
                "currency": currency,
                "timestamp": datetime.fromtimestamp(timestamp=data["prices"][i][0] / 1000, tz=pytz.UTC),
                "price": data["prices"][i][1],
                "market_cap": data["market_caps"][i][1],
                "total_volume": data["total_volumes"][i][1],
            })
        return coin_history

    def save_coin_history(self, history):
        for i in tqdm(range(len(history))):
            day_history = history[i]
            History.objects.update_or_create(
                **day_history
            )
