#!/usr/bin/env bash
# start-server.sh
(cd /app; python manage.py makemigrations && python manage.py migrate)
(cd /app; gunicorn id_dados_rio.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3 --log-level debug) &
nginx -g "daemon off;"
