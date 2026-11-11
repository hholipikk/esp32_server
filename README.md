# ESP32 Server

Минимальный backend на FastAPI для дальнейшей работы с ESP32.

## Запуск

В PowerShell перейдите в каталог проекта, создайте виртуальное окружение и установите зависимости:

```powershell
cd "$HOME\.pythonProjects\esp32_server"
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Активация окружения не обязательна, поэтому эта инструкция работает и при отключённом запуске PowerShell-сценариев.

Запустите сервер в режиме разработки:

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

После запуска:

- Проверка сервера: <http://127.0.0.1:8000/health>
- Интерактивная документация API: <http://127.0.0.1:8000/docs>

Проверка `/health` возвращает `{"status": "ok"}`. Маршруты для приема данных от ESP32 можно добавить по мере определения формата данных.
