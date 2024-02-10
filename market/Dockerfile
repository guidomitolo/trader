## builder stage

FROM python:3.8.5-slim-buster as builder

WORKDIR /usr/src/trader

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg \
    pkg-config \
    openssl \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install --upgrade pip wheel
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/trader/wheels -r requirements.txt

## final image stage

FROM python:3.8.5-slim-buster

RUN mkdir -p /home/trader

ARG DEFAULT_TZ='America/Argentina/Buenos_Aires'

ENV HOME=/home/trader
ENV APP_HOME=/home/trader/app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql \
    netcat

COPY --from=builder /usr/src/trader/wheels /wheels
COPY --from=builder /usr/src/trader/requirements.txt .
RUN pip install --no-cache /wheels/*

ENV TZ=${DEFAULT_TZ}

COPY ./entrypoint.sh .
COPY ./entrypoint_worker.sh .
COPY . $APP_HOME

RUN chmod +x  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint_worker.sh