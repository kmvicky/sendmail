sendzip
=======

Behold My Awesome Project!

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------
Run server: python manage.py runserver 8000

Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd sendzip
    worker: celery worker --app=sendzip.taskapp --loglevel=info
    
    To run celery please install redis-server.
    In case redis-server is having issue, please change CELERY_TASK_ALWAYS_EAGER = True and then instead of background it will work in for-ground.

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html




