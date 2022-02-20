# Create django project

$ `django-admin.py startproject projectname .`

# Create django App inside project

$ `docker-compose exec web django-admin.py startapp appname`

# Migration

$ `docker-compose exec web python manage.py makemigrations`

$ `docker-compose exec web python manage.py migrate`

# Build docker image

$ `docker-compose up -d --build`

# Run the migrations:

$ `docker-compose exec web python manage.py migrate --noinput`




## Navigate

 `http://localhost:8000/`
  
  to view the welcome screen



# For local dev
## Create virtual environment 
```bash
python3 -m venv env
```
```bash
source env/bin/activate
```

* Comment web section from services in docker-compose.yml file
* In .env file change you settings
```bash
DEBUG=1
SECRET_KEY=your_secret_key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=your_db_name
SQL_USER=your_username
SQL_PASSWORD=your_password
SQL_HOST=localhost
SQL_PORT=5440
DATABASE=postgres
```

* Go to Multiverse-app folder and RUN
```bash
docker-compose up -d --build
```

* Go to App folder and RUN
```bash
python3 manage.py runserver
```
