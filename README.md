# Telegram Bot для автоматизации услуг

Контейнеризованный Telegram-бот, который автоматизирует взаимодействие с пользователями, обрабатывает команды и поддерживает расписанную рассылку с использованием PostgreSQL для хранения данных.

## Функции

- **Обработка команд**
  - `/start`: Начало взаимодействия с ботом
  - `/help`: Показывает список команд
  - `/register`: Регистрация пользователя в базе данных

- **Автоответы**
  - Запросы цен
  - Информация о службе поддержки
  - Запросы каталогов

- **Основной функционал**
  - Рассылка сообщений по расписанию
  - Хранение данных в PostgreSQL
  - Контейнеризация с использованием Docker

## Технологический стек

- Python с python-telegram-bot
- PostgreSQL
- Docker & Docker Compose
- pytest с pytest-asyncio

## Установка

### Пререквизиты
- Docker и Docker Compose
- Токен Telegram-бота

### Настройка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/telegram-bot.git
cd telegram-bot
```

2. Отредактируйте файл `.env`, добавив данные для подключения к PostgreSQL:
```env
BOT_TOKEN=<Your Telegram Bot Token>
DB_USER=<Your Postgresql Username>
DB_PASSWORD=<Your Postgresql Password>
DB_NAME=botdb
DB_HOST=db
DB_PORT=5432
```

3. Запустите контейнеры:
```bash
docker-compose up -d
```

4. Если бот не реагирует:
```bash
docker-compose restart bot
```

### Проверка базы данных
```bash
docker exec -it postgres_db psql -U postgres -d botdb
\dt
SELECT * FROM users;
```

## Тестирование

Установите зависимости:
```bash
pip install -r requirements.txt
```

Запустите тесты:
```bash
pytest tests/
```

## Ключевые моменты дизайна

- **База данных**: PostgreSQL для масштабируемого хранения данных
- **Docker**: Оркестрация нескольких сервисов с проверкой состояния
- **Тестирование**: Комплексные тесты с использованием pytest
- **Код**: Модульная структура для удобства сопровождения

## Устранение неисправностей

**Бот неработоспособен**
```bash
docker-compose restart bot
```

**Проблемы с базой данных**
```bash
docker volume rm telegrambot_postgres_data
docker-compose up -d
```

**Просмотр логов**
```bash
docker-compose logs -f
```

## Будущие улучшения

- Добавление более сложных ответов с использованием обработки естественного языка
- Улучшение логирования и мониторинга с помощью Prometheus и Grafana
- Реализация аутентификации с помощью OAuth или API-ключей для дополнительной безопасности

## Вклад

Форк репозитория и отправляйте запросы на исправление ошибок.
