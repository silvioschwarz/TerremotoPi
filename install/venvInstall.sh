#! /bin/sh

sudo apt-get update
sudo apt-get upgrade

echo "install virtual environment and dependencies"
sudo apt-get install python3-venv

sudo ./modEnable.sh

#sudo python3.5 -m venv venv
sudo virtualenv venv
source venv/bin/activate

pip3 install -r requirements.txt
sudo ./plotlyPreRelease.sh
#sudo ./virtualHostInstall.sh

deactivate

