FROM python:3.6-buster
LABEL maintainer="qiwihui<qwh005007@gmail.com>"

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends --fix-missing supervisor \
    && pip install -r /tmp/requirements.txt \
    && apt-get clean \
    && rm -f /tmp/requirements.txt \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
