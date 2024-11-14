# Database Component

## Summary

Under construction

## Steps for build and run a single database

## 1. Create sql files:

Create a db folder and include the following files:

- `schema.sql`: Contains the SQL statements for create tables [using DDL]
- `data.sql`: Contains the SQL statements for insert initial data [using DML]

### 2. Create `Dockerfile`

Set postgres imagen base:
-  FROM postgres:16

Add lines for copy files into container:
- COPY ./db/schema.sql /docker-entrypoint-initdb.d/01_schema.sql
- COPY ./db/data.sql /docker-entrypoint-initdb.d/02_data.sql

### 3. Build database image

inside database folder:

```
docker build -t drytec/attenzio .
```

### 4. Run server with postgres

```
docker run --name attenzio -p 0.0.0.0:5432:5432 -e POSTGRES_PASSWORD=aP4sw0rd drytec/attenzio
```

### Run integrate with dockercompose






