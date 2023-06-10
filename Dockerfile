FROM python:3.10-slim
WORKDIR /app
EXPOSE 80
COPY * .
RUN pip install -U -r requirements.txt
CMD gunicorn --bind 0.0.0.0:80 wsgi:app