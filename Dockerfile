FROM python:3.12-slim

WORKDIR /app
COPY . /app
RUN python3 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV NAME FlaskApp

CMD ["gunicorn", "-b", "0.0.0.0:80", 'flask_app.py:app']