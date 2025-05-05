#!/bin/bash

# Wait for DB, migrate, etc. if needed

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the server
exec "$@"
