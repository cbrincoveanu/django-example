# Django Project

Django example with users, some data models, registration and login.

## Getting Started

Use conda to manage your environment.

```bash
# Create the environment from the YAML file
conda env create -f environment.yml

# Activate the environment
conda activate djangoprojectenv
```

After checking out the code from git, there won't be a database. In order for the web app to function, you will have to apply migrations first.
```bash
# optional; if models changed: python manage.py makemigrations app
python manage.py migrate
python manage.py createsuperuser # Admin user
```

Next, you can start the server.
```bash
python manage.py runserver
```

