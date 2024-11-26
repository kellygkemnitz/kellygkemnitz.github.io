FROM python:3.13-slim

WORKDIR /app

RUN python -m venv /opt/venv

SHELL ["/bin/bash", "-c"]
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -Ur requirements.txt

COPY static static/
COPY templates templates/
COPY app.py .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "1", "-k", "gevent", "--worker-connections", "500", "--timeout", "120", "--keep-alive", "5", "--log-level", "info", "--access-logfile", "-", "app:app"]
