# Backend Component

## Summary

Under construction

## Steps for build and run the backend


### 1. Create and activate python environment

Inside backend folder:

```
# Create the virtual environment
python -m venv env 
```

or

```
# Create the virtual environment
virtualenv -p python3 env
```

```
# Activate the virtual environment (Linux/Mac)
source env/bin/activate
```

```
# Activate the virtual environment (Windows)
env\Scripts\activate
```

### 2. Install dependencies

```
pip install -r requirements.txt
alternativamente 
python.exe -m pip install -r requirements.txt

```

### 3. Configure database connection

In the settings.py file, configure the database you want to use (SQLite is the default).

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pos_attenzio',
        'USER': 'postgres',
        'PASSWORD': 'database_password',
        'HOST': 'localhost',
        'PORT': '5000',
    }
}
```

### 4. Run the development server

```
python manage.py runserver
```


