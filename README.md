# tsaas-backend

- Homepage: [https://tsaas.iitr.ac.in](https://tsaas.iitr.ac.in)
- Wiki: [https://tsaas.iitr.ac.in/wiki](https://tsaas.iitr.ac.in/wiki)
- Privacy policy: [https://tsaas.iitr.ac.in/privacypolicy](https://tsaas.iitr.ac.in/privacypolicy)

# Development

### 1. Clone the repository

```bash
git clone https://github.com/teg-iitr/tsaas-backend
```

### 2. Create and activate a python3 virtual environment

```bash
python3 -m virtualenv --python=$(which python3) env
source env/bin/activate
```

To install `virtualenv`, follow the instructions from [here](https://virtualenv.pypa.io/en/latest/installation.html)

### 3. Install the required dependencies

```bash
cd tsaas-backend
pip install -r requirements.txt
```

### 4. Create local settings file and set up database

Sometimes, depending on your choice of database installing `postgresql` may also be required, which can be done following instructions for [MacOS](https://www.postgresqltutorial.com/install-postgresql-macos/), [Linux](https://www.postgresqltutorial.com/install-postgresql-linux/) and [Windows](https://www.postgresqltutorial.com/install-postgresql/)

We recommend using `postgresql` only in production environment, for development we recommend using `sqlite3` which comes pre-installed with `python`.

#### Creating local settings file

1. Inside folder `tsaas-backend/transport/settings` create a new file `local_settings.py`
2. Copy the content of the `production_settings.py` into `local_settings.py`
3. If you want to use `sqlite3` for database

   Inside file `local_settings.py`, comment line 97 to 107 and uncomment line 112 to 121

4. If you plan to use `postgresql`
   
    Configure your database in `local_settings.py` [line 97 to 107]

    ```python
    # ---> WE ARE USING POSTGRES AS RECOMMENDED BY DJANGO.
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name_of_database', # ---> REPLACE THIS WITH THE NAME OF YOUR OWN DATABASE
        'USER': 'dummy_username', # ---> REPLACE THIS WITH THE USERNAME YOU CREATE IN PSQL
        'PASSWORD': 'dummy_password', # ---> REPLACE THIS WITH THE PASSWORD YOU CREATE IN PSQL
        'HOST': 'localhost',
        'PORT': '',
        }
    }
    ```

### 5. Set up django

1. Apply migrations

```bash
python manage.py migrate
```

2. Create superuser for database
```bash
python manage.py createsuperuser
```

3. Make migrations for our `transdb` table
```bash
python manage.py makemigrations transdb
```

### 6. Start the Project

```bash
python manage.py runserver
```

To login to admin dashboard go to `http://127.0.0.1:8000/admin/` and login using the credentials you created using step 5.2
