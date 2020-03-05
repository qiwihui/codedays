#!/bin/bash
apt update -y
apt install -y supervisor
pip install -r requirements.txt
mkdir -p /var/log/celery/ /var/log/codeaday/
cp cad_server_*.conf /etc/supervisor/conf.d/
