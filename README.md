# Django REST Framework Examples

[![Python Tests](https://github.com/cyface/django-rest-framework-examples/actions/workflows/run_tests.yml/badge.svg)](https://github.com/cyface/django-rest-framework-examples/actions/workflows/run_tests.yml)

This repository is a companion to ["The Simplest Django REST Framework Example"](https://timlwhite.medium.com/the-simplest-django-rest-framework-example-c67cecc88400) article.

Specifically using as much of the automatic and generic views as possible.

This project includes a few apps implemented in different ways:

* `Games` is a simple bare-bones app that demonstrates the minimal DRF implmentation.
* `Podcasts` is a more full featured app with throttling, relations, and custom methods.

## How to get this running

* `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py loaddata games/fixtures/initial_data.json`
* `python manage.py loaddata podcasts/fixtures/initial_data.json`
* `python manage.py runserver`

Browse to : http://localhost:8000/podcasts/api/ or http://localhost:8000/games/api/ 
