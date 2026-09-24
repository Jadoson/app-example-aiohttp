# aiohttp

Пример приложения «Заметки» на [aiohttp](https://docs.aiohttp.org/): HTML-страница с формой, JSON API, статика и тесты.

## Структура

```
app.py              # точка входа
notes/
  config.py         # настройки из переменных окружения
  storage.py        # хранилище заметок в памяти
  templates/        # HTML-шаблоны
  static/           # CSS
tests/              # тесты (pytest)
```

Используется: aiohttp-jinja2 (Jinja2), middleware.

## Маршруты

| Метод  | Путь              | Описание                  |
|--------|-------------------|---------------------------|
| GET    | /                 | страница со списком       |
| POST   | /notes            | добавить заметку (форма)  |
| GET    | /api/notes        | список заметок (JSON)     |
| POST   | /api/notes        | создать заметку (JSON)    |
| GET    | /api/notes/{id}   | одна заметка              |
| DELETE | /api/notes/{id}   | удалить заметку           |
| GET    | /health           | проверка состояния        |

## Локальный запуск

```bash
pip install -r requirements.txt
python3 app.py
```

Приложение будет доступно на http://localhost:8080 (порт задаётся переменной `PORT`).

## Тесты

```bash
pip install -r requirements-dev.txt
pytest
```
