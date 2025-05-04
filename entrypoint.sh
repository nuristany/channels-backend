#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Run collectstatic
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run database migrations (optional but usually desired)
echo "Applying database migrations..."
python manage.py migrate

# Execute the main container command
exec "$@"
