## Requerimientos

* Python 3.5
* Python Virtualenv

## Docker

Requerimientos al usar Docker:

* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/)

```bash
cd docker/
docker-compose up
```

Url: `http://localhost:8000/API/countries/`

## Local

### Virtualenv (En linux)

#### Instalación

```bash
apt install virtualenv
```

#### Crear entorno

```bash
virtualenv -p python3 env
```

#### Activar entorno

```bash
source env/bin/activate
```

#### Instalar requerimientos

```bash
pip install -r requirements.txt
```

#### Ejecutar servidor

```bash
python manage.py runserver
```

Url: `http://localhost:8000/API/countries/`