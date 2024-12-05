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

EXPOSE 8081

CMD ["python3", "app"]
