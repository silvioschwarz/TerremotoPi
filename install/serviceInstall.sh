#! /bin/sh

echo "
[Unit]
Description=terremotopi
After=network.target

[Service]
User=pi
Restart=on-failure
WorkingDirectory=/home/TerremotoPi/
ExecStart=/home/pi/TerremotoPi/venv/bin/gunicorn -c /home/pi/gunicorn.conf -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
" >> terremotopi.service

sudo cp terremotopi.service /etc/systemd/system/terremotopi.service

sudo systemctl daemon-reload
sudo systemctl enable terremotopi
sudo systemctl start terremotopi

tail -f /var/log/syslog
