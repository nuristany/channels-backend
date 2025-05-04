# Dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install celery[redis] django-celery-beat
# Copy project files
COPY . .

# Correct CMD syntax
CMD ["uvicorn", "webchat.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--log-level", "debug", "--reload"]
