#! /bin/sh

sudo apt-get install python3-venv

sudo ./install/modEnable.sh

sudo python3.5 -m venv venv
#sudo virtualenv venv
#source venv/bin/activate

<<<<<<< HEAD
sudo -H pip3 install -r requirements.txt
=======
python3 -m pip install -r --user requirements.txt
>>>>>>> 90cf1c681b1eccef7fdc7ad4888d40927246d857
#sudo ./plotlyPreRelease.sh
#sudo ./virtualHostInstall.sh
python3 -m pip install --user adafruit_blinka adafruit-circuitpython-fxos8700 adafruit-circuitpython-fxas21002c

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
