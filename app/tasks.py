import time
import random
import redis
from celery import shared_task
from django.conf import settings
from .models import ImageModel
from services.send_telegram import send_telegram_message

redis_client = redis.Redis.from_url(settings.CELERY_BROKER_URL, decode_responses=True)

@shared_task
def process_single_image_task(record_id):
    time.sleep(20)
    number = random.randint(1, 1000)

    try:
        record = ImageModel.objects.get(id=record_id)
        record.number = number
        record.save()
    except ImageModel.DoesNotExist:
        return


@shared_task
def process_group_image_task(record_id, group_id):
    time.sleep(20)
    number = random.randint(1, 1000)

    try:
        record = ImageModel.objects.get(id=record_id)
        record.number = number
        record.save()
    except ImageModel.DoesNotExist:
        return

    redis_key = f'image_group_task_count:{group_id}'
    count = redis_client.incr(redis_key)

    if count % 20 == 0:
        chat_id = settings.TELEGRAM_CHAT_ID
        send_telegram_message(chat_id, f"Группа {group_id}: Обработано {count} фото!")

    if count == 100:
        redis_client.delete(redis_key)