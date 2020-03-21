# Blutspendekarte

## Overview
This project is a **work in progress**. It is part of the Hackathon `#wirvsvirus`.

## Installation
Dependencies:
- Python 3
- Flask
- Flask-RESTful
- PostgreSQL
- psycopg2

Install with:
```
git clone <url>
cd server
virtualenv -p python3 venv
source ven/bin/activate
pip install -r requirements.txt
```

## Config
The default config is in `config.py`.
This is then overwritten by the config specified by environment variable `BLUTSPENDEKARTE_CFG` (absolute path to the config file).
The path of the config file also specifies the working directory.
Example debugging config (in a folder called `instance`):
```
# Debugging config

DEBUG = True
```

## Running
This project consists of two endpoints: The REST-API behind `/api/` and the static pages on `/`.
Both must be provided by a server.
One example setup for debugging on Linux would be:
1. `python -m http.server 8000` in the `static` folder.
2. `BLUTSPENDEKARTE_CFG=/path/to/your/own/config.py python run.py`
3. A NGINX server proxying to both endpoints, e.g. using the following config:
```
# /etc/nginx/conf.d/blutspendekarte.cfg

server {
  listen 80;
  listen [::]:80;

  server_name localhost;

  root /home/t/projects/wirvsvirus/server/static;

  location /api/ {
    proxy_pass http://localhost:5000/api/;
  }

  location / {
    proxy_pass http://localhost:8000/;
  }

}

```
