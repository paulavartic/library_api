Library Management System API — это RESTful API, созданное с использованием Django и Django Rest Framework (DRF). Система предназначена для управления библиотекой, включая управление книгами, авторами, пользователями и отслеживание выдачи книг.

## Основной функционал

- **Управление книгами**:
  - Добавление, редактирование и удаление книг.
  - Получение списка книг с возможностью поиска по названию, автору и жанру.
- **Управление авторами**:
  - Добавление, редактирование и удаление авторов.
  - Получение списка авторов.
- **Управление пользователями**:
  - Регистрация и авторизация с использованием JWT токенов.
  - Получение информации о пользователях.
- **Выдача книг**:
  - Запись информации о выдаче книги пользователю.
  - Отправка уведомлений по электронной почте при выдаче книги.

## Используемые технологии

- **Backend**:
  - Django
  - Django Rest Framework (DRF)
- **База данных**:
  - PostgreSQL
- **Асинхронные задачи**:
  - Celery + Redis
- **Аутентификация**:
  - JWT токены (Django SimpleJWT)
- **Контейнеризация**:
  - Docker + Docker Compose
- **Документация API**:
  - OpenAPI (генерация с помощью drf-spectacular)

## Установка и запуск

### Требования

- Python 3.10+
- Docker и Docker Compose
- Redis

### Локальная установка

1. Клонируйте репозиторий:
   git clone 
   cd library-management-system
Установите зависимости:
pip install -r requirements.txt
Настройте .env файл: Создайте файл .env в корне проекта

Примените миграции:
python manage.py migrate

Запустите сервер разработки:
python manage.py runserver

Запустите Celery:
celery -A config worker --loglevel=info
Установка с Docker
Клонируйте репозиторий:
git clone 
cd library-management-system

Запустите проект с помощью Docker Compose:
docker-compose up --build
API будет доступно по адресу: http://localhost:8000.

Документация API
Документация API сгенерирована в формате OpenAPI и доступна по адресу:
http://localhost:8000/api/schema/swagger-ui/

Основные эндпоинты
Книги
Метод	URL	Описание
GET	/api/books/	Список всех книг
POST	/api/books/	Добавить новую книгу
GET	/api/books/{id}/	Получить информацию о книге
PUT	/api/books/{id}/	Редактировать книгу
DELETE	/api/books/{id}/	Удалить книгу
Авторы
Метод	URL	Описание
GET	/api/authors/	Список всех авторов
POST	/api/authors/	Добавить нового автора
GET	/api/authors/{id}/	Получить информацию об авторе
PUT	/api/authors/{id}/	Редактировать автора
DELETE	/api/authors/{id}/	Удалить автора
Выдача книг
Метод	URL	Описание
GET	/api/book-issues/	Список всех выдач
POST	/api/book-issues/	Выдать книгу пользователю
GET	/api/book-issues/{id}/	Получить информацию о выдаче
PUT	/api/book-issues/{id}/	Редактировать выдачу
DELETE	/api/book-issues/{id}/	Удалить запись о выдаче
Тестирование
Для запуска тестов используйте:
python manage.py test
