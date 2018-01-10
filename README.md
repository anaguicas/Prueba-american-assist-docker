## Requerimientos

* Python 3.5
* Python Virtualenv

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