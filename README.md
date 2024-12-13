# Pasos para correr el proyecto

## 1. Crear imagen

Dentro del folder "database"

```
docker build -t attenzio .
```

## 2. Correr contenedor

```
docker run --name attenzio -p 0.0.0.0:5432:5432 -e POSTGRES_PASSWORD=aP4sw0rd attenzio
```

## 3. Correr servidor de django

Dentro del folder "backend"

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


