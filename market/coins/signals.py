import time
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import History
  
@receiver(post_save, sender=History)
def delete_last_record(sender, instance, created, **kwargs):
    last_date = instance.timestamp - timedelta(days=89)
    last_records = sender.objects.filter(coin=instance.coin, timestamp__lte = last_date)
    last_records.delete()