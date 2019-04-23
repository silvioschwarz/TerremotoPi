#! /bin/sh

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install -y build-essential python-dev python-smbus

python3 -m pip install --user RPi.GPIO setuptools

sudo apt-get install -y i2c-tools

# enable i2c spi
ls /dev/i2c* /dev/spi*

echo "/dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1"

#use python3

echo "INSTALL CIRCUIT PYTHON"

python3 -m pip install --user adafruit_blinka adafruit-circuitpython-fxos8700 adafruit-circuitpython-fxas21002c

