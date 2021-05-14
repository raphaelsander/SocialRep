# Project SocialRep

## First Use

### Create virtual environment

```bash
python -m venv venv
```

### Install dependencies

```bash
pip install -r src/requirements.txt
```

### Make migrations

```bash
python manage.py makemigrations
```

### Migrate

```bash
python manage.py migrate
```

### Create admin user

```bash
python manage.py createsuperuser
```