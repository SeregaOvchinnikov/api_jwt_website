# API_JWT_Website

## Описание проекта api_jwt_website
В проекте аутентификация происходит по JWT токену. Описана модель Follow, в которой два поля — user (кто подписан) и following (на кого подписан). Для этой модели в документации описан эндпоинт /follow/ и два метода:
GET — возвращает все подписки пользователя, сделавшего запрос. Возможен поиск по подпискам по параметру search.
POST — подписать пользователя, сделавшего запрос на пользователя, переданного в теле запроса. При попытке подписаться на самого себя, пользователь получает сообщение об ошибке. Проверка осуществляется на уровне API.
Анонимный пользователь на запросы к этому эндпоинту получает ответ с кодом 401 Unauthorized.


## Используемые технологии
- Python 3.11
- SQLite3
- Django REST Framework
- API REST
- Postman
- Simple-JWT

## Подготовка к запуску и запуск проекта api_jwt_website
Клонирование репозитория:

```
git clone git@github.com:ваш-аккаунт-на-гитхабе/api_jwt_website.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate 
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнение миграций:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver

```
## Документация

Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация

Тестировать и добавлять данные удобно после прохождения авторизации через Postman.

### Примеры запросов к API

Для доступа к API необходимо получить JWT-токен: выполнить POST-запрос localhost:8000/api/v1/token/, передав поля username и password.

При дальнейшей отправке запросов токен передается в заголовке Authorization: Bearer <токен>

Примеры обращения к методам и ответов:

1)

/api/v1/posts/ (GET, POST)

ответ API на GET-запрос:

{ 
  "count": 123, 
  "next": "http://api.example.org/accounts/?offset=400&limit=100", 
  "previous": "http://api.example.org/accounts/?offset=200&limit=100", 
  "results": [ 
    { 
      "id": 0, 
      "author": "string", 
      "text": "string", 
      "pub_date": "2023-04-16T20:41:29.648Z", 
      "image": "string", 
      "group": 0 
    } 
  ] 
} 
POST-запрос:

{ 
  "text": "string", 
  "image": "string", 
  "group": 0 
} 
ответ API на POST-запрос:

{ 
  "id": 0, 
  "author": "string", 
  "text": "string", 
  "pub_date": "2023-04-16T20:45:29.648Z", 
  "image": "string", 
  "group": 0 
} 

2)

/api/v1/groups/ (GET)

ответ API на GET-запрос:

[ 
  { 
    "id": 0, 
    "title": "string", 
    "slug": "string", 
    "description": "string" 
  } 
]

#### Автор: Сергей Овчинников
