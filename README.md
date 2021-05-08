# Django REST Framework Examples
Simple Django REST Framework Examples

Specifically using as much of the automatic and generic views as possible.

This project includes a few apps implemented in different ways:

* `Games` is a simple bare-bones implementation that demonstrates the minimal DRF implmentation.
* `Podcasts` is a more full featured app with throttling, relations, and custom methods.

## How to get this running

* `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py loaddata podcasts/fixtures/initial_data.json`
* `python manage.py runserver`

Browse to : http://localhost:8000/api/podcasts/
