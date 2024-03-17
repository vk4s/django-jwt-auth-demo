# Django Restframework demo with JWT Authentication
An application to demostrate JWT based api authentican in rest apis.
---

# Testing
There are unittests for the apis.
Run the following command to test the API
```sh
python src/manage.py test
```

# Run
| _--insecure_ to allow automated handeling static assets. (Not to be used outside localhost)
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



