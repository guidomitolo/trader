## Coin Trader App

### Components

1. Django framework and ORM to manage the db
2. Django Rest Framework to build the api
3. Celery to fullfill async backend tasks
4. CoinGecko endpoints via env variables
5. Front created with create-react-app
5.a. react app with Lazy Loading and Write Through caching strategies
6. Styles with bootstrap
7. Charts with Charts.js
8. pyenv versions as a python env manager

### Run

Project directory structure

```
./
├── coin-market
│   ├── Dockerfile
│   ├── nginx
│   │   └── nginx.conf
│   ├── node_modules
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   │   ├── favicon.ico
│   │   └── index.html
│   ├── src
│   │   ├── components
│   │   │   ├── async.js
│   │   │   ├── cache.js
│   │   │   ├── charts
│   │   │   │   ├── chart.js
│   │   │   │   └── index.js
│   │   │   ├── home
│   │   │   │   └── home.js
│   │   │   └── table
│   │   │       └── index.js
│   │   ├── error.js
│   │   ├── index.css
│   │   ├── index.js
│   │   └── routes.js
│   └── tailwind.config.js
├── docker-compose.yml
├── market
│   ├── coins
│   │   ├── admin.py
│   │   ├── api.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── management
│   │   │   ├── commands
│   │   │   │   ├── import_coins.py
│   │   │   │   ├── import_history.py
│   │   │   │   └── load_currencies.py
│   │   │   └── __init__.py
│   │   ├── middleware
│   │   │   ├── __init__.py
│   │   │   └── requests.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_alter_history_unique_together_and_more.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── signals.py
│   │   ├── tasks.py
│   │   ├── tests.py
│   │   └── urls.py
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── entrypoint_worker.sh
│   ├── manage.py
│   ├── market
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── requirements.txt
└── README.md

4854 directories, 41156 files (cache and npm mod included)
```

**Prerequisites**

- [docker client](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)

**Instalation**

1. Clone the repository

`git clone https://github.com/guidomitolo/trader`

2. Create a `.env` file at root and set the following environment variables<sup>[1](#detail)</sup>:

```
DBNAME=marketdb
DBUSER=postgres
DBPORT=5432
DBHOST=db
DBPASS=topSecretPass

DEBUG=True
REDIS_HOST=redis://broker

POSTGRES_USER=postgres
POSTGRES_PASSWORD=topSecretPass
POSTGRES_DB=marketdb

API_RECALL_MINUTES=15
```

**Deploy**

Deploy the application by running: `docker-compose up -d`.

After docker-compose is successfully deployed the application will be locally available via:

http://localhost/


### Public endpoints
#### (authentication not required)

|Route|DRF View|Method|
|-|-|-|
| 🟩 /api/coin/ | CoinViewSet | GET |
| 🟩 /api/coin/ | CoinViewSet | GET |
| 🟩 /api/history/ | HistoryViewSet | GET |
| 🟩 /api/history/{coin}/ | HistoryViewSet | GET |
| 🟩 /api/history/{coin}/draw/{days}/ | HistoryViewSet | GET |

----

<a name="detail">1</a>: suggested env vars (these can be modified)