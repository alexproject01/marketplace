# Online marketplace.

 - Product catalog with filters and sort parameters.
 - Detailed page for product with description, images, prices from different sellers and reviews 
(authorized user can add a review)
 - Products comparison
 - Personal account for users (registration, email confirmation, log-in\out, password reset, 
profile info, orders history)
 - Cart for products (authorized and unauthorized user)
 - Discount mechanism integrated with cart (discounts per product/cart/set)
 - Order form, delivery price calculation
 - Online payments with Yookassa (Yandex) API (a service for online payment acceptance)
 - Administrative section for sellers

# Installation

## install pre-commit
    create - .pre-commit-config.yaml
    pip install pre-commit
    pre-commit install(устанавливаем нашу настройку)

## running Celery
    pip install -r requirements.txt
    celery -A shope worker --loglevel=info

## Website translation
    python manage.py makemessages -l ru - сгенерировать переводы на русский язык
    python manage.py makemessages -l en - сгенерировать переводы на English
    python manage.py compilemessages - скомпиллировать переводы

## Apply fixtures
    python manage.py apply_fixtures - применить все фикстуры

## Running imports
    python manage.py run_imports - запустить импорты всех файлов в директории imports/expected_imports
    python manage.py run_imports -p <file_1> <file_2> <file_3> -e <email> - запустить импорт указанных файлов и уведомить о завершении по данному email

## Running django-silk
    pip install -r requirements.txt - для установки пакетов django-silk и gprof2dot
    python manage.py migrate - для миграций silk
    http://127.0.0.1:8000/silk/requests/ - url адрес для просмотра запросов

## Running docker
    docker compose up -d --build - сборка перед стартом контейнеров
    docker compose up -d - запуск контейнеров (-d для запуска в фоне)
    docker compose down - остановка контейнеров
