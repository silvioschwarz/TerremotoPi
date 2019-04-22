import datetime 
import time   
import board
import busio
import adafruit_fxos8700

from plotly.graph_objs import Scatter, Layout, Figure

import plotly
import plotly.plotly as py  
import plotly.tools as tls   
from plotly.graph_objs import *
 
import numpy as np 


username = 'slvschwrz'
api_key = '8XzVPYd7tK4xOY95PYc3'


py.sign_in(username, api_key)

stream_ids = tls.get_credentials_file()['stream_ids']

stream_id= stream_ids[0]


stream1 = scatter.Stream(
    token= stream_ids[0],
    maxpoints=800     
)

trace1 = Scatter(
    x=[],
    y=[],
    name='X',
    mode='lines+markers',
    stream=stream1        
)


stream2 = scatter.Stream(
    token= stream_ids[1],  
    maxpoints=800     
)



trace2 = Scatter(
    x=[],
    y=[],
    name='Y',
    mode='lines+markers',
    stream=stream2        
)


stream3 = scatter.Stream(
    token= stream_ids[2],  
    maxpoints=800     
)



trace3 = Scatter(
    x=[],
    y=[],
    name='Z',
    mode='lines+markers',
    stream=stream3        
)


stream4 = scatter.Stream(
    token= stream_ids[3],  
    maxpoints=800    
)



trace4 = Scatter(
    x=[],
    y=[],
    name='Temperature',
    mode='lines+markers',
    stream=stream4        
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


fig = Figure(data=trace1, layout=layout)
print py.plot(fig, filename='Raspberry Pi Streaming Example Values')

#unique_url = py.plot(fig, filename='s7_first-stream')

s = py.Stream(stream_ids[0])
#t = py.Stream(stream_ids[1])
#u = py.Stream(stream_ids[2])
#v = py.Stream(stream_ids[3])


s.open()
#t.open()
#u.open()
#v.open()


 
i = 0
k = 5
N = 800

time.sleep(5) 

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)


while True:
	accel_x, accel_y, accel_z = sensor.accelerometer
	x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

	s.write(dict(x=x, y=accel_x))  
#	t.write(dict(x=x, y=accel_y))  
#    	u.write(dict(x=x, y=accel_z))  
#	v.write(dict(x=x, y=accel_x))  

        i += 1

        time.sleep(0.25)


s.close() 
#t.close()
#u.close()
#v.close()
