from rest_framework import viewsets, permissions, authentication
from .models import History, Coin
from .serializers import HistorySerializer, CoinSerializer
import logging
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from drf_spectacular.openapi import OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from datetime import datetime, timedelta
import pytz
from .tasks import update_coin_history
from django.conf import settings
from rest_framework.decorators import action

logger = logging.getLogger(__name__)


class HistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [permissions.AllowAny]
    authentication = [authentication.BasicAuthentication]
    lookup_field = "coin"
    lookup_value_regex = "[^/]+" 
    
    def get_updated_queryset(self, coin, currency):
        coin = Coin.objects.filter(code=coin).first()
        last_record = self.queryset.order_by('timestamp').last()

        if last_record:
            last_timestamp = last_record.timestamp
            now = datetime.now(tz=pytz.UTC)
            until = (now - timedelta(days=1))
            if (now - last_timestamp).seconds / 60 > settings.API_RECALL_MINUTES:
                update_coin_history.delay(coin.code, currency, until)

        return self.queryset.filter(coin=coin).order_by('timestamp')

    @extend_schema(
        parameters=[OpenApiParameter("page", OpenApiTypes.INT, OpenApiParameter.QUERY, required=False, description="A page number within the paginated result set."),],
        responses=HistorySerializer(many=True)
    )
    @method_decorator(cache_page(60*5)) # 5 minutes backend cache
    def retrieve(self, request, coin, currency="usd", *args, **kwargs):
        queryset = self.get_updated_queryset(coin, currency)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=["get"], url_path="draw/(?P<days>\d+)")
    def retrieve_draw(self, request, coin, currency="usd", days="2", *args, **kwargs):
        now = datetime.now(tz=pytz.UTC)
        queryset = self.get_updated_queryset(coin, currency).filter(timestamp__gte=(now - timedelta(days=int(days))))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CoinViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    permission_classes = [permissions.AllowAny]
    authentication = [authentication.BasicAuthentication]