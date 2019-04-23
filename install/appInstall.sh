#! /bin/sh

sudo apt-get install python3-venv

sudo ./modEnable.sh

sudo python3.5 -m venv venv
#sudo virtualenv venv
#source venv/bin/activate

sudo -H pip3 install -r requirements.txt
#sudo ./plotlyPreRelease.sh
#sudo ./virtualHostInstall.sh

#deactivate

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

python3 -m pip install adafruit-circuitpython-fxos8700 --user
python3 -m pip install adafruit-circuitpython-fxas21002c --user
