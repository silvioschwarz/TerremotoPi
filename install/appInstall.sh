#! /bin/sh

sudo apt-get install python3-venv

sudo mkdir app

cd app

sudo python3.5 -m venv flaskvenv
source flaskvenv/bin/activate


sudo python app.py


SERVICE="
[Unit]
Description=terremotopi
After=network.target

[Service]
User=flaskappuser
Restart=on-failure
WorkingDirectory=/home/pi/Documents/Terremotopi/app/
ExecStart=/home/pi/Documents/Terremotopi/app/flaskvenv/bin/gunicorn -c /home/pi/Documents/Terremotopi/app/gunicorn.conf -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
"

echo "$SERVICE" | sudo tee /etc/systemd/system/terremotopi.service
