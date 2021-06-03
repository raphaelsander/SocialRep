# Project SocialRep

## First Use

Prefer use in [Docker](#to-run-in-docker) instead set up your environment.

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

---

## To run in Docker

### Build the image

```bash
docker build -t socialrep .
```

*Before build in Windows, it's need change the line separator in docker-entrypoint.sh file to LF instead CRLF.*

### Execute the container

```bash
docker run --name socialrep -d -e SECRET_KEY=test -e DEBUG=True -p 80:8000 socialrep
```

Reference: <https://docs.docker.com/engine/reference/commandline/run/>

*Now you can access the web application in your [localhost](http:localhost)*

### Environment Variables

| Env. Variables | Values                           | Examples                      | Descriptions                                                                    |
|----------------|----------------------------------|-------------------------------|---------------------------------------------------------------------------------|
| ALLOWED_HOSTS  | IPv4/IPv6 IP Address or HostName | 192.168.0.101,127.0.0.1,[::1] | https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/#allowed-hosts |
| DEBUG          | True or False                    | True                          | https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/#debug         |
| SECRET_KEY     | String                           | my_secret_key                 | https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/#secret-key    |
