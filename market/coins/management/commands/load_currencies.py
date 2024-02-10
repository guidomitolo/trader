from django.core.management import BaseCommand
from ...models import Currency


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(f"Begin import currencies")
        try:
            currencies = [
                {"code":"ars", "name": "Peso"},
                {"code":"usd", "name": "Dollar"},
                {"code":"eur", "name": "Euro"},
            ]
            for currency in currencies:
                Currency.objects.create(name=currency["name"], code=currency["code"])
            self.stdout.write(self.style.SUCCESS("Currencies import successfull"))
        except Exception as error:
            print(error)
            self.stdout.write(self.style.ERROR("Currencies import failed"))


