FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gcc \
    && apt-get clean

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/staticfiles && chown -R www-data:www-data /app/staticfiles
RUN ls -la /app/static
RUN pwd
RUN python manage.py collectstatic --noinput

ENV DJANGO_SETTINGS_MODULE=image_service.settings

CMD ["gunicorn", "image_service.wsgi:application", "--bind", "0.0.0.0:8000"]