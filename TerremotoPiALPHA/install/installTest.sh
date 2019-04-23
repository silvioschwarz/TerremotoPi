#! /bin/sh

sudo apt-get update
sudo apt-get upgrade


#Hello blinka!
#Digital IO ok!
#i2c ok!
#spi ok!
#done !
#




echo "import board
import busio
import adafruit_bmp280
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
print('Temperature: {} degrees C'.format(sensor.temperature)) 
print('Pressure: {}hPa'.format(sensor.pressure))
sensor.sea_level_pressure = 1013.25
print('Altitude: {} meters'.format(sensor.altitude))" > bmp280.py

python bmp280.py
#https://github.com/adafruit/Adafruit_CircuitPython_BMP280





#NXP Precision 9DoF Breakout

echo "import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c
i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)
print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.accelerometer))
print('Magnetometer (uTesla): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.magnetometer))
print('Gyroscope (radians/s): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxas.gyroscope))" > NXP.py

python NXP.py


echo "# Simple demo of the FXAS21002C gyroscope.
# Will print the gyroscope values every second.
import time

import board
import busio

import adafruit_fxas21002c


# Initialize I2C bus and device.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxas21002c.FXAS21002C(i2c)
# Optionally create the sensor with a different gyroscope range (the
# default is 250 DPS, but you can use 500, 1000, or 2000 DPS values):
#sensor = adafruit_fxas21002c.FXAS21002C(i2c, gyro_range=adafruit_fxas21002c.GYRO_RANGE_500DPS)
#sensor = adafruit_fxas21002c.FXAS21002C(i2c, gyro_range=adafruit_fxas21002c.GYRO_RANGE_1000DPS)
#sensor = adafruit_fxas21002c.FXAS21002C(i2c, gyro_range=adafruit_fxas21002c.GYRO_RANGE_2000DPS)

# Main loop will read the gyroscope values every second and print them out.
while True:
# Read gyroscope.
gyro_x, gyro_y, gyro_z = sensor.gyroscope
# Print values.
print('Gyroscope (radians/s): ({0:0.3f},  {1:0.3f},  {2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
# Delay for a second.
time.sleep(1.0)
" > NXPGyro.py

python NXPGyro.py

echo "# Simple demo of the FXOS8700 accelerometer and magnetometer.
# Will print the acceleration and magnetometer values every second.
import time

import board
import busio

import adafruit_fxos8700


# Initialize I2C bus and device.
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)
# Optionally create the sensor with a different accelerometer range (the
# default is 2G, but you can use 4G or 8G values):
#sensor = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_4G)
#sensor = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_8G)

# Main loop will read the acceleration and magnetometer values every second
# and print them out.
while True:
# Read acceleration & magnetometer.
accel_x, accel_y, accel_z = sensor.accelerometer
mag_x, mag_y, mag_z = sensor.magnetometer
# Print values.
print('Acceleration (m/s^2): ({0:0.3f}, {1:0.3f}, {2:0.3f})'.format(accel_x, accel_y, accel_z))
print('Magnetometer (uTesla): ({0:0.3f}, {1:0.3f}, {2:0.3f})'.format(mag_x, mag_y, mag_z))
# Delay for a second.
time.sleep(1.0)
" > NXPAccMag.py


python NXPAccMag.py


sudo apt install python3-smbus





