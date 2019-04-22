<<<<<<< HEAD
import time
=======
import datetime 
import time   
>>>>>>> 6efa1648701806a5c0c85870be5358ef64e28b43
import board
import busio
import adafruit_fxos8700
import datetime

<<<<<<< HEAD
import plotly
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import numpy as np

py.sign_in('slvschwrz', '8XzVPYd7tK4xOY95PYc3')
=======
from plotly.graph_objs import Scatter, Layout, Figure

import plotly
import plotly.plotly as py  
import plotly.tools as tls   
from plotly.graph_objs import *
 
import numpy as np 
>>>>>>> 6efa1648701806a5c0c85870be5358ef64e28b43


username = 'slvschwrz'
api_key = '8XzVPYd7tK4xOY95PYc3'


py.sign_in(username, api_key)

stream_ids = tls.get_credentials_file()['stream_ids']

stream_id= stream_ids[0]
<<<<<<< HEAD
stream1 = scatter.Stream(
    token= stream_ids[0],
    maxpoints=800
)


=======


stream1 = scatter.Stream(
    token= stream_ids[0],
    maxpoints=800     
)

>>>>>>> 6efa1648701806a5c0c85870be5358ef64e28b43
trace1 = Scatter(
    x=[],
    y=[],
    name='X',
    mode='lines+markers',
<<<<<<< HEAD
    stream=stream1
)

stream2 = scatter.Stream(
    token= stream_ids[1],
    maxpoints=800
)

=======
    stream=stream1        
)


stream2 = scatter.Stream(
    token= stream_ids[1],  
    maxpoints=800     
)



>>>>>>> 6efa1648701806a5c0c85870be5358ef64e28b43
trace2 = Scatter(
    x=[],
    y=[],
    name='Y',
    mode='lines+markers',
<<<<<<< HEAD
    stream=stream2
)

stream3 = scatter.Stream(
    token= stream_ids[2],
    maxpoints=800
)


=======
    stream=stream2        
)


stream3 = scatter.Stream(
    token= stream_ids[2],  
    maxpoints=800     
)



>>>>>>> 6efa1648701806a5c0c85870be5358ef64e28b43
trace3 = Scatter(
    x=[],
    y=[],
    name='Z',
    mode='lines+markers',
<<<<<<< HEAD
    stream=stream3
)

stream4 = scatter.Stream(
    token= stream_ids[3],
    maxpoints=800
)


=======
    stream=stream3        
)


stream4 = scatter.Stream(
    token= stream_ids[3],  
    maxpoints=800    
)



>>>>>>> 6efa1648701806a5c0c85870be5358ef64e28b43
trace4 = Scatter(
    x=[],
    y=[],
    name='Temperature',
    mode='lines+markers',
<<<<<<< HEAD
    stream=stream4
=======
    stream=stream4        
>>>>>>> 6efa1648701806a5c0c85870be5358ef64e28b43
)



data = ([trace1, trace2, trace3])


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

<<<<<<< HEAD
fig = Figure(data=data, layout=layout)

unique_url = py.plot(fig, filename='s7_first-stream')
=======

fig = Figure(data=trace1, layout=layout)
print py.plot(fig, filename='Raspberry Pi Streaming Example Values')
>>>>>>> 6efa1648701806a5c0c85870be5358ef64e28b43

#unique_url = py.plot(fig, filename='s7_first-stream')

s = py.Stream(stream_ids[0])
#t = py.Stream(stream_ids[1])
#u = py.Stream(stream_ids[2])
#v = py.Stream(stream_ids[3])


s.open()
#t.open()
#u.open()
#v.open()


<<<<<<< HEAD
###############################################

i = 0
k = 5
N = 800

time.sleep(5)
=======
 
i = 0
k = 5
N = 800

time.sleep(5) 
>>>>>>> 6efa1648701806a5c0c85870be5358ef64e28b43

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)


while True:
<<<<<<< HEAD
#while i<N:
#sensor = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_4G)
#sensor = adafruit_fxos8700.FXOS8700(i2c, accel_range=adafruit_fxos8700.ACCEL_RANGE_8G)


    accel_x, accel_y, accel_z = sensor.accelerometer
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

#    i+=1

    s.write(dict(x=x, y=accel_x))
    t.write(dict(x=x, y=accel_y))
    u.write(dict(x=x, y=accel_z))
    v.write(dict(x=x, y=accel_x))
    time.sleep(0.1)

s.close()
t.close()
u.close()
v.close()
=======
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
>>>>>>> 6efa1648701806a5c0c85870be5358ef64e28b43
