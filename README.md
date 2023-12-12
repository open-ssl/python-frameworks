# python-frameworks
All start samples for Python frameworks with Docker-compose deployment


### Frameworks routes table: 

| Framework |             Address              |                                                                       
|-----------|:--------------------------------:|
| FastAPI   | [127.0.0.1:3000](127.0.0.1:3000) |
| Django    | [127.0.0.1:3001](127.0.0.1:3001) |
| Flask     | [127.0.0.1:3002](127.0.0.1:3002) |
| Aiohttp   | [127.0.0.1:3003](127.0.0.1:3003) |
| Tornado   | [127.0.0.1:3004](127.0.0.1:3004) |
| Pyramid   | [127.0.0.1:3005](127.0.0.1:3005) |
| CherryPy  | [127.0.0.1:3006](127.0.0.1:3006) |


### How to Start?
`docker-compose up --build`

### Install virtual environment with commands:
1. `python3 -m venv venv`
2. `source venv/bin/activate`

### How to Create FastAPI project?
1. `pip install -r requirements.txt`
2. Create and describe `main.py` file

#### Start FastAPI application:
- `python main.py` 
- Using `uvicorn main:app --reload` with default `PORT=8000` 
- Using `uvicorn main:app --host 0.0.0.0 --port 3001` with project config

### How to Create Django project?
1. `pip install -r requirements.txt`
2. `django-admin startproject django_framework` 
3. `cd django_framework && python manage.py startapp django_app`
4. Add new app in `django_framework/settings.py` INSTALLED_APPS const
5. Create view in `django_app/views.py` 
6. `mkdir django_app/templates/` 
7. `touch django_app/templates/root.html` and describe html
8. Set app url in `django_framework/urls.py`
9. `touch django_app/urls.py` and set url
10. Set `DEBUG = False` and `ALLOWED_HOSTS` in `django_framework/settings.py`
11. Hide `SECRET_KEY` from `django_framework/settings.py`

#### Start Django application:
- `python manage.py runserver`

### How to Create Flask project?
1. `pip install -r requirements.txt`
2. Create and describe `main.py` file
3. Create `wsgi.py` file with `gunicorn` start config (production start config)

#### Start Flask application:
- `python main.py` 
- Using default start Flask command: `flask run` 
- Using `gunicorn --bind 0.0.0.0:$PORT wsgi:app`

### How to Create AioHTTP project?
1. `pip install -r requirements.txt`
2. Create and describe `app/routes.py` file
3. Create and describe `main.py` file

#### Start AioHTTP application:
- `python main.py`

### How to Create Tornado project?
1. `pip install -r requirements.txt`
2. Create and describe `views/views.py` file
3. Create and describe `main.py` file

#### Start Tornado application:
- `python main.py`

### How to Create Pyramid project?
1. `pip install -r requirements.txt`
2. Create and describe `main.py` file

#### Start Pyramid application:
- `python main.py`

### How to Create CherryPy project?
1. `pip install -r requirements.txt`
2. Create and describe `main.py` file

#### Start CherryPy application:
- `python main.py`