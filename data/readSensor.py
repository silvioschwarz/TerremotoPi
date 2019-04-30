#!/usr/bin/env python
import numpy as np
import pandas as pd
import time
import board
import busio
import adafruit_fxos8700
import sqlite3
from datetime import *

 
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)

connex = sqlite3.connect("acceleration-data.db")  # Opens file if exists, else creates file
cursor = connex.cursor()

now = dt.datetime.now()
sec = now.second
minute = now.minute
hour = now.hour
microsec = now.microsecond
 
try:
	accel_x, accel_y, accel_z = sensor.accelerometer
	totalTime = ((hour * 3600) + (minute * 60) + (sec)) *1000 + (microsec)
    cursor.execute ("INSERT INTO acceleration (datum, uhrzeit, ACCX,ACCY,ACCZ,TOTALTIME) VALUES (CURRENT_DATE(), NOW(), %.2f, %.2f,%.2f,%.2f);" % accel_x, accel_y, accel_z,totaltime)
    db.commit()
    print("Done")
except:
    print("Error. Rolling back.")
    db.rollback()
