#!/bin/sh
if [ "$DBNAME" = "marketdb" ]; then
    echo "Bringing up $DBNAME"

    while ! nc -z $DBHOST $DBPORT; do
      sleep 0.5
    done

    echo "$DBNAME started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py createcachetable
python manage.py collectstatic
python manage.py load_currencies
python manage.py import_coins
python manage.py import_history
gunicorn market.wsgi:application --bind 0.0.0.0:8000

exec "$@"