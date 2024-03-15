FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/static

EXPOSE 8000

# Set command to run Django development server and collect static files
CMD ["python", "manage.py", "collectstatic", "--no-input", && "python", "manage.py", "runserver", "0.0.0.0:8000"]
