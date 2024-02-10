from django.core.management import BaseCommand
from ...models import Coin
from django.conf import settings
from tqdm import tqdm
import requests
import json


class Command(BaseCommand):

    full_api_endpoint = f"{settings.API_COINGECKO}list"

    def handle(self, *args, **options):
        print(f"Begin import coins")
        try:
            response = requests.get(self.full_api_endpoint)
            coins = json.loads(response.content)

            my_coins_filter = settings.COIN_LIST
            my_coins = list(filter(lambda x: x["id"] in my_coins_filter, coins))

            self.save_coins(my_coins)
            self.stdout.write(self.style.SUCCESS('Coins import successfull'))
        except Exception as error:
            print(error)
            self.stdout.write(self.style.ERROR('Coins import failed'))

    def save_coins(self, coins):
        for i in tqdm(range(len(coins))):
            coin = coins[i]
            Coin.objects.get_or_create(code=coin["id"], name=coin["name"])



    