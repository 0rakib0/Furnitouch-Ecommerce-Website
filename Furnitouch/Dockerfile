FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1         
WORKDIR /app
COPY . /app
COPY .env /app/.env
RUN apt-get update && apt-get install -y \
    libpq-dev gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip3.8 install --upgrade pip && \
    pip3.8 install -r requirements.txt

EXPOSE 8080
CMD ["python3.8", "manage.py", "runserver", "0.0.0.0:8080"]