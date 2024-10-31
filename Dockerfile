FROM python:3.12-slim

WORKDIR /app
COPY . /app
RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "1", "-k", "gevent", "--worker-connections", "500", "--timeout", "120", "--keep-alive", "5", "--log-level", "info", "--access-logfile", "-", "flask_app:app"]
