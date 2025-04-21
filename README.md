# tron-test
# Сервис для работы с tronpy


## Запуск проекта

### Предварительные требования
- Python 3.12
- [UV](https://github.com/astral-sh/uv) (установите через `pip install uv`)
- Docker и Docker Compose (для запуска через контейнеры ЖЕЛАТЕЛЬНО)

### Установка
1. Создайте виртуальное окружение:
```bash
uv venv  # Создаст виртуальное окружение в .venv
Для Linux/MacOS

  source .venv/bin/activate
Или для Windows:

  .venv\Scripts\activate
```

2. Синхронизируйте библиотеки:
```bash
uv sync
```

3. Создайте файл .env с данными из env_example
```bash
cp .env_example .env
```

4. Запуск сервиса
```bash
make up
```

5. Запуск линтеров
```bash
make linters
```

6. Запуск тестов
Перед запуском тестов нужно создать test_db вручную в pgadmin. Для этого нужно перейти на http://127.0.0.1:5050/ логин и пароль указаны в .env


И создать БД с названием test_db


Затем запустить
```bash
make test
```

# Эндпоинты
1. Получить список запросов
Выведется список всех запросов с повторами, такая реализация, чтобы можно было отследить изменения в кошельке

GET http://127.0.0.1:8000/api/wallet/requests

2. Получить информацию о кошельке
POST http://127.0.0.1:8000/api/wallet
```json
{
	"wallet_address": ""
}
```
