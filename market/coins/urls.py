from django.urls import path
from rest_framework.routers import SimpleRouter
from .api import *

router = SimpleRouter() 

router.register('coin', CoinViewSet, basename='coin')
router.register('history', HistoryViewSet, basename='history')