up:
	@gunicorn --bind 0.0.0.0:80 wsgi:app

dev:
	@gunicorn --reload wsgi:app