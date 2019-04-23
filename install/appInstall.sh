#! /bin/sh

sudo apt-get install python3-venv

sudo ./install/modEnable.sh
./pythonInstall.sh

echo '
accesslog = "./logs/gunicorn_access.log"
errorlog = "./logs/gunicorn_error.log"' >> gunicorn.conf

mkdir logs

WSGI="
#!/usr/bin/python
import sys
sys.path.insert(0,"/var/www/html/seismology/terremotopi/")
from app import app as application
"
echo "$WSGI" | sudo tee /var/www/html/seismology/terremotopi/terremotopi.wsgi

