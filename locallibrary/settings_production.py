from decouple import config, Csv
ALLOWED_HOSTS = ['.vercel.app']
DEBUG = True
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": config("POSTGRES__PGHOST"),
        "PORT": 5432,
        "NAME": config("POSTGRES__PGDATABASE"),
        "USER": config("POSTGRES__PGUSER"),
        "PASSWORD": config("POSTGRES__PGPASSWORD")
    }
}
