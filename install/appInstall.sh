#! /bin/sh

sudo apt-get install python3-venv

sudo ./modEnable.sh

#sudo python3.5 -m venv venv
sudo virtualenv venv
source venv/bin/activate

sudo -H pip3 install -r requirements.txt
sudo ./plotlyPreRelease.sh
#sudo ./virtualHostInstall.sh

deactivate

echo '
accesslog = "/home/pi/Documents/Earthquake-Distances/logs/gunicorn_access.log"
errorlog = "/home/pi/Documents/Earthquake-Distances/logs/gunicorn_error.log"' > gunicorn.conf

mkdir logs

SERVICE="
[Unit]
Description=terremotopi
After=network.target

[Service]
User=pi
Restart=on-failure
WorkingDirectory=/home/pi/Documents/Terremotopi/app/
ExecStart=/home/pi/Documents/Terremotopi/venv/bin/gunicorn -c /home/pi/Documents/Terremotopi/gunicorn.conf -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
"

echo "$SERVICE" | sudo tee /etc/systemd/system/terremotopi.service


systemctl daemon-reload
systemctl enable terremotopi
systemctl start terremotopi

WSGI="
#!/usr/bin/python
import sys
sys.path.insert(0,"/var/www/html/terremotopi/")
from app import app as application
"
echo "$WSGI" | sudo tee /var/www/html/terremotopi/terremotopi.wsgi

