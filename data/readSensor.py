#!/usr/bin/env python
import numpy as np
import pandas as pd
import time
import board
import busio
import adafruit_fxos8700
import sqlite3
import datetime as dt

def readSensor():
	i2c = busio.I2C(board.SCL, board.SDA)
	sensor = adafruit_fxos8700.FXOS8700(i2c)

	now = dt.datetime.now()
	sec = now.second
	minute = now.minute
	hour = now.hour
	microsec = now.microsecond
	totaltime = ((hour * 3600) + (minute * 60) + (sec))*1000 + microsec

	accelx, accely, accelz = sensor.accelerometer
	df = pd.DataFrame.from_dict({'Time': [totaltime], 'X': [accelx], 'Y':[accely],'Z':[accelz]})

	db = sqlite3.connect("accelerationDB.db")
	cursor = db.cursor()
	cursor.execute("DROP TABLE IF EXISTS acceleration")

	df.to_sql(name='acceleration', con=db)

if __name__ == '__main__':
	readSensor()

#print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f},{3})'.format(accelx, accely, accelz, totaltime))
