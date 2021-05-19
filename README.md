# Project SocialRep

## First Use

### Install pip

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

Reference: <https://pip.pypa.io/en/stable/installing/>

### Create virtual environment

```bash
python -m pip install venv
```

```bash
python -m venv venv
```

### Active virtual env

*For Linux*

```bash
source venv/Scripts/active
```

*For Windows Prompt*

```bat
venv\Scripts\active.bat
```

*For Windows PowerShell*

```ps1
venv\Scripts\active.ps1
```

Reference: <https://docs.python.org/pt-br/3/library/venv.html>

### Install dependencies

```bash
pip install -r src/requirements.txt
```

### Make migrations

```bash
python manage.py makemigrations
```

Reference: <https://docs.djangoproject.com/en/3.2/topics/migrations/>

### Migrate

```bash
python manage.py migrate
```

### Create admin user

```bash
python manage.py createsuperuser
```