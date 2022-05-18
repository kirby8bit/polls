# polls
 1) docker-compose up -d
 2) source env/bin/activate
 3) python manage.py migrate
 4) python manage.py runserver
 
Чтобы можно было добавлять опросы, нужно перед этим завести админа:
  python manage.py createsuperuser
