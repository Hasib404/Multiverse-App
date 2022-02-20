# Create virtual environment 
$ `python3 -m venv env`

$ `source env/bin/activate`

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