# django-blog

A Blog made to learn Django and try things.

# Local development environment

    python3 -m venv venv
    . ./venv/bin/activate
    pip install -r requirements.txt
    
## Run

    cd bloggy
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    