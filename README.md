# Telegram Bot for Service Automation

A containerized Telegram bot that automates user interactions, processes commands, and supports scheduled broadcasting using PostgreSQL for data persistence.

## Features

- **Command Processing**
  - `/start`: Initiates bot interaction
  - `/help`: Shows commands list
  - `/register`: Database user registration

- **Auto-Responses**
  - Price inquiries
  - Support information
  - Catalog requests

- **Core Functionality**
  - Scheduled message broadcasting
  - PostgreSQL data persistence
  - Docker containerization

## Tech Stack

- Python with python-telegram-bot
- PostgreSQL
- Docker & Docker Compose
- pytest with pytest-asyncio

## Installation

### Prerequisites
- Docker and Docker Compose
- Telegram bot token

### Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/telegram-bot.git
cd telegram-bot
```

2. Edit the `.env` file to include your postgres credentials:
```env
BOT_TOKEN=<Your Telegram Bot Token>
DB_USER=postgres
DB_PASSWORD=123
DB_NAME=botdb
DB_HOST=db
DB_PORT=5432
```

3. Launch containers:
```bash
docker-compose up -d
```

4. In case the bot is unresponsive:
```bash
docker-compose restart bot
```

### Database Verification
```bash
docker exec -it postgres_db psql -U postgres -d botdb
\dt
SELECT * FROM users;
```

## Testing

Install dependencies:
```bash
pip install -r requirements.txt
```

Run tests:
```bash
pytest tests/ 
```

## Design Highlights

- **Database**: PostgreSQL for scalable data storage
- **Docker**: Multi-service orchestration with health checks
- **Testing**: Comprehensive pytest suite
- **Code**: Modular organization for maintenance

## Troubleshooting

**Bot Unresponsive**
```bash
docker-compose restart bot
```

**Database Issues**
```bash
docker volume rm telegrambot_postgres_data
docker-compose up -d
```

**View Logs**
```bash
docker-compose logs -f
```

## Future Improvements

- Add more sophisticated responses using natural language processing
- Improve logging and monitoring with tools like Prometheus and Grafana.
- Implement OAuth or API key authentication for additional security.

## Contributing

Fork repository and submit pull requests for contributions.


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
