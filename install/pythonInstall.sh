#! /bin/sh

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install -y build-essential python-dev python-pip python-smbus python3-pip

pip3 install --user RPi.GPIO setuptools

sudo apt-get install -y i2c-tools

# enable i2c spi
ls /dev/i2c* /dev/spi*

echo "/dev/i2c-1 /dev/spidev0.0 /dev/spidev0.1"

#use python3

echo "INSTALL CIRCUIT PYTHON"

pip3 install --user adafruit-blinka

