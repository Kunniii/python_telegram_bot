up:
	@gunicorn wsgi:app

dev:
	@gunicorn --reload wsgi:app