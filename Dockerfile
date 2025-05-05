FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install celery[redis] django-celery-beat

# Copy project files
COPY . .

# Create static directory
RUN mkdir -p /app/staticfiles

ENV RUNNING_IN_DOCKER_BUILD=1
# ✅ Collect static files
RUN python manage.py collectstatic --noinput

# Add entrypoint
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

# For production, do not use --reload
CMD ["uvicorn", "webchat.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--log-level", "debug"]
