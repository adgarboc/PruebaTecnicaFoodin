#!/bin/sh

echo "Waiting for database..."
while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
  sleep 0.1
done
echo "Database started"
python manage.py migrate
python manage.py init_superuser \
--username="$DJANGO_SUPERUSER_USERNAME" \
--password="$DJANGO_SUPERUSER_PASSWORD" \
--email="$DJANGO_SUPERUSER_EMAIL"
exec "$@"