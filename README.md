# LEARN TO WORK DJANGO SIGNALS AND MIXINS (DB sqlite3)

## django signals worked pre_save, post_save, pre_delete and post_delete
## Mixins like ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
````doctest
quickly build API views that map closely database models.
reuse the mixins and flexible composition of behavior.
````

## Create virtual environment and activated it.

## Requirements
### Python - 3 and above
### Django and DRF

````python
    Installation:
    
    pip install -r requirements.txt
    
    Database migration
    
    python manage.py makemigrations
    
    python manage.py migrate
    
    python manage.py runserver
````
## Below REST api requests all using curl.
## URL for GET,POST,PUT and DELETE  worked url details

````python
    http://127.0.0.1:8000/task
    http://127.0.0.1:8000/task/id/
    http://127.0.0.1:8000/task/date
    http://127.0.0.1:8000/task/date/id/
    http://127.0.0.1:8000/history/
    http://127.0.0.1:8000/history/id/
    http://127.0.0.1:8000/history/date
    http://127.0.0.1:8000/history/date/id/
````