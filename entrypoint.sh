#!/bin/bash

echo "Waiting for database ${DB_HOST}:${DB_PORT} to be ready..."
holdup -t 30.0 -i 0.1 "tcp://${DB_HOST}:${DB_PORT}"

python manage.py migrate
python manage.py runserver 0.0.0.0:8000