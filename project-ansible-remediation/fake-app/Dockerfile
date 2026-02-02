FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates ./templates

EXPOSE 8080

# default version
ENV APP_VERSION=1.2
ENV APP_NAME="Fake Service"

CMD ["python", "app.py"]