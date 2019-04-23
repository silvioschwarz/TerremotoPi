#-*- coding: utf-8 -*-
#import plotly 
#plotly.tools.set_credentials_file(username='VioS', api_key='JMMHBi0nZDKLpbiDuMJ7', stream_ids=[r8tha6hsk3])

import time

import board
import busio

import adafruit_fxos8700


import plotly
 
plotly.__version__

import plotly.plotly as py  
import plotly.tools as tls   
from plotly.graph_objs import *
import numpy as np  # (*) numpy for math functions and arrays

stream_ids = tls.get_credentials_file()['stream_ids']


# Get stream id from stream id list 
stream_id= stream_ids[0]
# Make instance of stream id object 
stream1 = scatter.Stream(
    token= stream_ids[0],  # (!) link stream id to 'token' key
    maxpoints=800      # (!) keep a max of 80 pts on screen
)


# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = Scatter(
    x=[],
    y=[],
    name='X',
    mode='lines+markers',
    stream=stream1         # (!) embed stream id, 1 per trace
)

# Make instance of stream id object 
stream2 = scatter.Stream(
    token= stream_ids[1],  # (!) link stream id to 'token' key
    maxpoints=800      # (!) keep a max of 80 pts on screen
)


# Initialize trace of streaming plot by embedding the unique stream_id
trace2 = Scatter(
    x=[],
    y=[],
    name='Y',
    mode='lines+markers',
    stream=stream2         # (!) embed stream id, 1 per trace
)

# Make instance of stream id object 
stream3 = scatter.Stream(
    token= stream_ids[2],  # (!) link stream id to 'token' key
    maxpoints=800      # (!) keep a max of 80 pts on screen
)


# Initialize trace of streaming plot by embedding the unique stream_id
trace3 = Scatter(
    x=[],
    y=[],
    name='Z',
    mode='lines+markers',
    stream=stream3         # (!) embed stream id, 1 per trace
)

# Make instance of stream id object 
stream4 = scatter.Stream(
    token= stream_ids[3],  # (!) link stream id to 'token' key
    maxpoints=800     # (!) keep a max of 80 pts on screen
)


# Initialize trace of streaming plot by embedding the unique stream_id
trace4 = Scatter(
    x=[],
    y=[],
    name='Temperature',
    mode='lines+markers',
    stream=stream4         # (!) embed stream id, 1 per trace
)



data = ([trace1, trace2, trace3])


# Add title to layout object
layout = Layout(title='Time Series',
	xaxis=dict(
        	title='Time',
        	titlefont=dict(
            		family='Courier New, monospace',
            		size=18,
            		color='#7f7f7f'
        		)
    		),
    	yaxis=dict(
        	title='Acceleration [m/S²]',
       		 titlefont=dict(
            		family='Courier New, monospace',
            		size=18,
            		color='#7f7f7f'
        		),
		range=[-5, 15]
		),
	autosize=False,
    	width=900,
    	height=600
	)

fig = Figure(data=data, layout=layout)

unique_url = py.plot(fig, filename='s7_first-stream')


s = py.Stream(stream_ids[0])
t = py.Stream(stream_ids[1])
u = py.Stream(stream_ids[2])
v = py.Stream(stream_ids[3])

# (@) Open the stream
s.open()
t.open()
u.open()
v.open()

# (*) Import module keep track and format current time
import datetime 
import time   
 
i = 0    # a counter
k = 5    # some shape parameter
N = 800  # number of points to be plotted

# Delay start of stream by 5 sec (time to switch tabs)
#time.sleep(5)

print("START!") 

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)

#while True:
while i<N:
#sensor = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_4G)
#sensor = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_8G)
    accel_x, accel_y, accel_z = sensor.accelerometer
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    i+=1
    print("DATA INCOMING")
    s.write(dict(x=x, y=accel_x))  
    t.write(dict(x=x, y=accel_y))  
    u.write(dict(x=x, y=accel_z))  
    v.write(dict(x=x, y=accel_x))  

#    time.sleep(0.01)
s.close() 
t.close()
u.close()
v.close()
