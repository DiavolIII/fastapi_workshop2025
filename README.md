# FastAPI Workshop Project

Проект, объединяющий пройденные темы курса: разработка программных модулей

Автор: **Danya Bangert (DiavolIII)**

Структура: **Переделана под более комфортную для автора**

---

## Основные функции

-  **RESTful API** для управления товарами (CRUD)
-  **Аутентификация через JWT-токены**
-  **SQLite + SQLAlchemy (асинхронный ORM)**
-  **Миграции с Alembic**
-  **Валидация данных через Pydantic**
-  **Чистая архитектура**: роутеры, репозитории, зависимости
-  **Middleware** для логирования запросов
-  **Логирование** с помощью Loguru

---

## Фаст запуск

### Требования
- Python 3.10+
- pip

### Установка и запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/ваш-логин/fastapi-workshop-project.git
cd fastapi-workshop-project

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Применить миграции
alembic upgrade head

# 4. Запустить сервер
uvicorn app.main:app --reload
