from django.core.management import BaseCommand
from django.conf import settings
from ...tasks import CoinGeckoApiConnection


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(f"Begin import history")

        try:
            coins = settings.COIN_LIST
            for coin in coins:
                api_connection = CoinGeckoApiConnection(coin, 'usd')
                api_connection.save_updated_coin_data()
            self.stdout.write(self.style.SUCCESS("Coin's History import successfull"))
        except Exception as error:
            print(error)
            self.stdout.write(self.style.ERROR("Coin's History import failed"))






    