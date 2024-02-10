import logging


logger = logging.getLogger(__name__)


class APIRequestCount:

    count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if '/api/history' in request.path:
            self.count += 1
            logger.info(f'History Requested nro: {self.count}')
    
        return self.get_response(request)