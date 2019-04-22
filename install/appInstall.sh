#! /bin/sh

sudo apt-get install python3-venv

sudo ./install/modEnable.sh

sudo python3.5 -m venv venv
#sudo virtualenv venv
source venv/bin/activate

python3 -m pip install -r --user requirements.txt
#sudo ./plotlyPreRelease.sh
#sudo ./virtualHostInstall.sh
python3 -m pip install --user adafruit_blinka adafruit-circuitpython-fxos8700 adafruit-circuitpython-fxas21002c

deactivate

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

