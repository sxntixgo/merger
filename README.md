# merger
**Important:** Merger has been desiged for and tested in Kali LInux 2020.1

## Preparations
In order to install merger, you need to clone this repository and make sure you have all the system dependencies installed.

### System dependences

Before installing make sure you have the following packages installed:

```bash
sudo apt-get update
sudo apt-get install git python3 python3-pip python3-venv python3-dev libpq-dev postgresql openssl -y
sudo pip3 install virtualenv
```

### Cloning

The following command will clone merger:

```bash
git clone https://github.com/sxntixgo/merger.git
```

## Install
The following are the instructions to install merger in Kali Linux 2020.1

### Create and activate virtual environment

Activate the virtual environment with the following commands

```bash
cd merger
virtualenv venv
source venv/bin/activate
```

### Install merger dependencies

The following command will install the requirements for merger:

```bash
pip install -r merger/requirements.txt
```

### Setup the dababase

Generate keys for the web application and the dabatase with:

```bash
SECRET_KEY=$(openssl rand -base64 32)
DB_SECRET=$(openssl rand -base64 32)
```

**Important:** update `merger/merger/settings/local.py` with these two keys.

Then, create the user and database in postgres:

```bash
sudo service postgresql start
sudo -u postgres psql -c "CREATE DATABASE merger;"
sudo -u postgres psql -c "CREATE USER merger WITH PASSWORD '"$DB_SECRET"';"
sudo -u postgres psql -c "ALTER ROLE merger SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE merger SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE merger SET timezone TO 'UTC';"
```

### Make migrations and migrate

Make django migrations with the following command:

```bash
python merger/manage.py makemigrations main --settings=merger.settings.local
```

Migrate

```bash
python merger/manage.py migrate --settings=merger.settings.local
```

## Run

### Activate your virtual environment
If it is not activated, activate your virtual environment with:

```bash
cd merger
source venv/bin/activate
```

### Run the web server
```bash
python merger/manage.py runserver --settings=merger.settings.local
```

### Access merger
By default the merger will run at http://127.0.0.1:8080