# merger
***Important:** Merger has been desiged for and tested in Kali LInux 2020.2*

## Docker

Docker install is straight forward as it automatically install all the requirements.

### Preparations

Install the dependencies with:

```bash
sudo apt-get update
sudo apt-get install curl python3 -y
```

Install docker using this tutorial: https://medium.com/@airman604/installing-docker-in-kali-linux-2017-1-fbaa4d1447fe

Install `docker-compose` using this tutorial: https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-debian-10

Clone the repository with:

```bash
git clone --depth 1 https://github.com/sxntixgo/merger.git
```

***Note:** we use `depth -1` to clone the latest version of merger*

### Generate `.env` file and additional directories

The `.env` file must contain the password for the DB and the Web application. The `media` directory contains two more directories: `reports` and `uploads`. The `static` directory will contain all the static files served by nginx. You can generate all of them with:

```bash
cd merger
python3 setup.py
```

### Build and run the images

To build and run the images, execute (you might need use sudo):

```bash
sudo docker-compose up
```

### Access the application

Open a browser and go to http://0.0.0.0:8080

## Virtual Environment

### Preparations
In order to install merger, you need to clone this repository and make sure you have all the system dependencies installed.

#### System dependences

Before installing make sure you have the following packages installed:

```bash
sudo apt-get update
sudo apt-get install git python3 python3-pip python3-venv python3-dev libpq-dev postgresql openssl -y
```

#### Cloning

The following command will clone merger:

```bash
git clone https://github.com/sxntixgo/merger.git
```

### Install
The following are the instructions to install merger in Kali Linux 2020.2

#### Create and activate virtual environment

Activate the virtual environment with the following commands

```bash
cd merger
python3 -m venv venv
source venv/bin/activate
```

#### Install merger dependencies

The following command will install the requirements for merger:

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Generate `.env` file and additional directories

The `.env` file must contain the password for the DB and the Web application. The `media` directory contains two more directories: `reports` and `uploads`. The `static` directory will contain all the static files served by nginx. You can generate all of them with:

```bash
cd merger
python3 setup.py
```

#### Setup the dababase

Create the user and database in postgres:

```bash
sudo service postgresql start
sudo -u postgres psql -c "CREATE DATABASE merger;"
sudo -u postgres psql -c "CREATE USER merger WITH PASSWORD '"$DB_PASSWORD"';"
sudo -u postgres psql -c "ALTER ROLE merger SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE merger SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE merger SET timezone TO 'UTC';"
```

#### Migrate the database

Migrate changes to the database

```bash
python manage.py migrate
```

#### Change debug config

If you are running this locally, you need to change `DEBUG = False` to `DEBUG = True` from `meger/settings.py` (line 24), since Django's does not serve static files when not in debug mode.

If you want to run the venv setup on a production environment, check the following page: https://djangocentral.com/deploy-django-with-nginx-gunicorn-postgresql-and-lets-encrypt-ssl-on-ubuntu/


### Run

#### Activate your virtual environment
If it is not activated, activate your virtual environment with:

```bash
cd merger
source venv/bin/activate
```

#### Run the web server

The web server will run with:

```bash
python manage.py runserver
```

#### Access merger

By default the merger will run at http://127.0.0.1:8080