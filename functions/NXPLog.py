from datetime import datetime
import time
import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c
i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)

fileName = "./logs/log-"+datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S"+".csv")
file = open(fileName, "a")
file.write(datetime.now().strftime("%Y%m%d-%H%M%S")+","+\
	"Acceleration X (m/s^2),Acceleration Y (m/s^2),Acceleration Z (m/s^2)"+","+\
	"Magnetometer X (uTesla), Magnetometer Y (uTesla)  , Magnetometer Z (uTesla)"+","+\
	"Gyroscope X (radians/s), Gyroscope Y (radians/s), Gyroscope Z (radians/s)")

while True:
# Read acceleration & magnetometer.
	acc = '{0:0.3f},{1:0.3f},{2:0.3f}'.format(*fxos.accelerometer)
	magneto='{0:0.3f},{1:0.3f},{2:0.3f}'.format(*fxos.magnetometer)
	gyro = '{0:0.3f},{1:0.3f},{2:0.3f}'.format(*fxas.gyroscope)

	data = datetime.utcnow().strftime("%Y-%m-%d-%H:%M:%S.%f") + ","+acc + ","+magneto+","+gyro+"\n"
	file.write(data)
	file.flush()
	time.sleep(0.1)
file.close()
