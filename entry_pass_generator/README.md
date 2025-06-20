# Entry Pass Generator

Приложение автоматизирует создание служебной записки на въезд и отправку её в службу безопасности.

## Установка

```bash
poetry install
```

## Переменные окружения

Создайте файл `.env` со значениями:

```
SMTP_HOST=<smtp host>
SMTP_PORT=<smtp port>
SMTP_USER=<smtp user>
SMTP_PASS=<smtp password>
SECURITY_EMAIL=<email получателя>
```

## Запуск

```bash
uvicorn entry_pass_generator.webhook:app --reload
```

После запуска перейдите на `/start`, чтобы увидеть стартовую страницу с
кнопкой "Старт" и 3D-анимацией. Нажатие на кнопку откроет форму создания
служебной записки.

## Пример запроса

```bash
curl -X POST http://localhost:8080/webhook \
    -H "Content-Type: application/json" \
    -d '{"full_name":"Иванов И.И.","vehicle_plate":"A123BC77","start_date":"2024-01-01","end_date":"2024-01-02","purpose":"Доставка оборудования"}'
```
