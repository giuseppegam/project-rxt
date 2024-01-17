#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

while ! nc -z $DATABASES['default']['ENGINE'] $DATABASES['default']['PORT']; do
  echo "🟡 Waiting for Postgres Database Startup ($DATABASES['default']['ENGINE'] $DATABASES['default']['PORT']) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($DATABASES['default']['ENGINE']:$DATABASES['default']['PORT'])"

python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py migrate --database=waze --noinput
python manage.py runserver 0.0.0.0:8000