#! /bin/sh

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install build-essential python-dev python-pip python3-pip -y
sudo apt-get install python-smbus -y

sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools

# enable i2c spi
ls /dev/i2c*

# /dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1

#use python3

echo "INSTALL CIRCUIT PYTHON"
python3 -m pip install --user setuptools -U
python3 -m pip install --user RPI.GPIO
python3 -m pip install --user adafruit_blinka
python3 -m pip install --user adafruit-circuitpython-bmp280
python3 -m pip install --user adafruit_blinka -U
python3 -m pip install --user adafruit-circuitpython-fxos8700
python3 -m pip install --user adafruit-circuitpython-fxas2100c
python3 -m pip install --user mpu6050-raspberrypi

python blinkatest.py

