#!/bin/sh
python3 -m celery -A market worker -l info
exec "$@"