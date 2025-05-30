# 📦 Image Service

Django-приложение для загрузки, хранения и массовой обработки изображений. Поддерживает интеграцию с Telegram-ботом, Celery, Redis, PostgreSQL и Yandex S3.

## 🧰 Стек технологий

- **Версия языка**: Python 3.13
- **Backend**: Django, Django REST Framework  
- **База данных**: PostgreSQL  
- **Очереди задач**: Celery + Redis  
- **Хранение**: Yandex Object Storage (S3-совместимое хранилище)  
- **Бот**: Telegram Bot API  
- **Тестирование**: pytest  (пока не готово)
- **Контейнеризация**: Docker, Docker Compose

---

## 🚀 Страт проекта

1. **Клонируйте репозиторий**:

   ```bash
   https://github.com/twentyonetima/image_uploader.git
   cd image_service
   ```
   
2. **Создайте .env файл**:
   ```bash
    #TELEGRAM
    
    TELEGRAM_BOT_TOKEN=7394901642:AAGVL2uB2JY2UbWnT8dpY8iPIW0ff8WbhsU
    TELEGRAM_CHAT_ID=-1002608170329
    
    #POSTGRESQL
    
    POSTGRES_DB=image_service
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    
    #CELERY+REDIS
    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
    
    #SECRET_KEY
    SECRET_KEY=django-insecure-let4obf9_u3kx@53uej=ynftwffk78kseoin%+^a4s2bj+xb(^
    
    #YANDEX_OBJECT_STORAGE
    
    YANDEX_ACCESS_KEY=YANDEX_ACCESS_KEY     #(прикреплю отдельно)
    YANDEX_SECRET_KEY=YANDEX_SECRET_KEY     #(прикреплю отдельно)
    YANDEX_BUCKET_NAME=YANDEX_BUCKET_NAME   #(прикреплю отдельно)
   ```
   
3. **Соберите и запустите контейнеры**:

   ```bash
    docker-compose up --build
   ```

Проект будет доступен по адресу: http://localhost:8000

4. **Посмотреть оповещение о удачной загрузке 20 изображений можно по ссылке**:

    ```bash
    https://t.me/+xwKApHk8Q6ZlNTFi
    ```

---

## 📂 Основной функционал
- Загрузка изображений через API

- Хранение изображений в Yandex S3

- Обработка изображений и массовая обработка изображений через Celery

- Telegram-бот для оповещения о успешной загрузке 20 изображений

- REST API для получения и обработки изображений

- Немного фронта с использованием HTML, JS, CSS