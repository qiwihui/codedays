#!/bin/bash
apt update -y
apt install -y supervisor
pip install -r requirements.txt
mkdir -p /var/log/celery/ /var/log/codedays/
cp cad_server_*.conf /etc/supervisor/conf.d/
patch -p0 --forward /usr/local/lib/python3.6/site-packages/django/db/backends/mysql/operations.py < mysql_operations.patch || true
