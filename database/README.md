
# 1. Build database image

inside database folder:

```
docker build -t attenzio .
```

# 2. Run container

```
docker run --name attenzio -p 0.0.0.0:5432:5432 -e POSTGRES_PASSWORD=aP4sw0rd attenzio
```

# 3. From backend folder run django server

```
python manage.py runserver 0.0.0.0:8000
```

# 4. From frontend folder run project 

```
npm start
```


