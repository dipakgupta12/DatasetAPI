VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -fr venv

venv:
	$(VIRTUALENV) venv

setup: venv
	. venv/bin/activate; pip install -r requirements.txt
	. venv/bin/activate; python manage.py migrate --sync-db

run-dev:
	. venv/bin/activate; python manage.py runserver

run-stage:
	. venv/bin/activate; python manage.py runserver --settings=datasetapi.settings.staging

run-prod:
	. venv/bin/activate; python manage.py runserver --settings=datasetapi.settings.prod