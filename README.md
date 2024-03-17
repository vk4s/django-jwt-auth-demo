# Django Restframework demo with JWT Authentication
An application to demostrate JWT based authentication for rest apis.

---

# Requirements
- Python >= 3.11
- Database: Sqlite3

# Testing
There are unittests for the apis.
Run the following command to test the application
```sh
python src/manage.py test
```

# Run

### 1. Docker compose
```sh
docker compose up -d
```

### 2. Docker Hub
Directly run from Dockerhub
```sh
docker run noxcoder99/django-jwt-demo:1.0.0 -p 8000:8000
```
Then access: [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.


### 3. Locally
| _--insecure_ to allow automated handeling static assets. (Not to be used outside localhost)
```sh
pip install -r requirements.txt
```

```sh
python src/manage.py makemigrations && python src/manage.py migrate
```

```sh
python src/manage.py createsuperuser
```

```sh
python src/manage.py collectstatic --noinput
```

```sh
python src/manage.py runserver 0.0.0.0:8000 --insecure
```


# API Testing Commands

## Create user
```sh
curl --request POST \
  --url http://127.0.0.1:8000/api/v1/register/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnium/0.2.3-a' \
  --data '{
"username":"test5",
"email": "test@example.com",
"password":"Vikash@123"
}'
```

## Login user
```sh
curl --request POST \
  --url http://127.0.0.1:8000/api/v1/login/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnium/0.2.3-a' \
  --data '{
"username":"test5",
"email": "test@example.com",
"password":"Vikash@123"
}'
```

## Logout (Doesn't apply to JWT based stateless tokens)
```sh
curl --request POST \
  --url http://127.0.0.1:8000/api/v1/logout/ \
  --header 'Authorization: JWT <YOU_ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnium/0.2.3-a'
```

## Verify a JWT token
```sh
curl --request GET \
  --url http://127.0.0.1:8000/api/v1/verify-token/ \
  --header 'Authorization: Token <YOU_ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnium/0.2.3-a'
```

## Refresh Token (get a new access token)
```sh
curl --request POST \
  --url http://127.0.0.1:8000/api/v1/token/refresh/ \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnium/0.2.3-a' \
  --data '{
	"refresh": "<YOUR_REFRESH_TOKEN>"
}'
```




# Docker commands

## Build and tag the image
```sh
docker build --tag django-jwt-demo:1.0.0 .
```

```sh
docker tag django-jwt-demo:1.0.0 django-jwt-demo:latest
```


