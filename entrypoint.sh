#!/bin/sh

echo "🏁 ENTRYPOINT STARTED"

set -e

echo "📦 Running collectstatic..."
python manage.py collectstatic --noinput

echo "🛠 Running migrate..."
python manage.py migrate

exec "$@"
