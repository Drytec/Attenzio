FROM postgres:16
COPY ./db/database.sql /docker-entrypoint-initdb.d/00_database.sql
COPY ./db/schema.sql /docker-entrypoint-initdb.d/01_schema.sql
# PLPSQL
COPY ./db/plpsql.sql /docker-entrypoint-initdb.d/02_plpsql.sql
COPY ./db/data.sql /docker-entrypoint-initdb.d/03_data.sql


