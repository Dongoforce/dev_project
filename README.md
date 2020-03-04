# dev_project
# Инструкция по запуску проекта

Что бы запустить проект в docker, в директорию /dev_project нужно положить 2 файла

.env.prod

```
DATABASE_URL=postgres://postgres:login@postgres_db:5432/project_db
SECRET_KEY=
DJANGO_APP_DEBUG=True
```
SECRET_KEY можно получить from django.core.management.utils import get_random_secret_key

postgres.env

```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=project_db
```

Далее нужно выполнить команды:

```
docker-compose build
docker-compose run --rm app_cont bash -c "python manage.py collectstatic --no-input; python manage.py migrate"
docker-compose up
```
и перейта на http://localhost:8080/

Для запуска проекта без docker

В директорию /dev_project нужно положить 1 файл

В pgAdmin нужно создать базу данных с названием project_db

.env

```
DATABASE_URL=postgres://login:password@localhost:5432/project_db
SECRET_KEY=
DJANGO_APP_DEBUG=True
```

И выполнить команды:

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
и перейта на http://localhost:8000/

Для запуска тестов:

```
python manage.py test
```
