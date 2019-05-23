import datetime
import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c
i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)


Acceleration (m/s^2):
Magnetometer (uTesla):
Gyroscope (radians/s):

while True:
# Read acceleration & magnetometer.
	acc = '({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.accelerometer)
	magneto='({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.magnetometer)
	gyro = '({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxas.gyroscope)
	now = datetime.now()
	data = acc + ","+magneto+","+gyro+","+time
	time.sleep(1.0)
