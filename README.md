# AutoService Desk

Веб-сервіс онлайн-запису на технічне обслуговування авто з Docker-контейнеризацією та CI/CD.

## Технологічний стек
- Frontend: HTML5, CSS3, JavaScript (WCAG AA).
- Backend / Web Server: Nginx 1.25 Alpine у Docker.
- Тестування: Python 3.11, unittest, beautifulsoup4.
- CI/CD: GitHub Actions (.github/workflows/ci.yml).

## Архітектура (C4 Context & Container)
- Клієнт звертається через веб-браузер до порту 8080.
- Nginx передає статичний інтерфейс та забезпечує маршрутизацію.
- GitHub Actions автоматично тестує інтерфейс при змінах у гілці main.

## Запуск та тестування
```bash
docker compose up -d --build
pip install -r requirements.txt
python test_ui.py
