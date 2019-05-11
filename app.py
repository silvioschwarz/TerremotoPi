#! /bin/python3

import plotly
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs.layout as lo

#import pandas as pd
#import numpy as np
from flask import Flask
import os
import sqlite3
import datetime as dt

import board
import busio
import adafruit_fxos8700

#https://github.com/plotly/dash-wind-streaming

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "https://fonts.googleapis.com/css?family=Raleway:400,400i,700,700i",
                "https://fonts.googleapis.com/css?family=Product+Sans:400,400i,700,700i"]


app = dash.Dash(
    'streaming-acceleration',
    external_stylesheets=external_css
)

#app.config.update({
    # as the proxy server will remove the prefix
#    'routes_pathname_prefix': '/terremotopi/',

    # the front-end will prefix this string to the requests
    # that are made to the proxy server
#    'requests_pathname_prefix': '/terremotopi/'
#})

app.config.requests_pathname_prefix = ''
server = app.server

#app.css.config.serve_locally = True
#app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div([
        html.H2("Acceleration Streaming"),
    ], className='banner'),
    html.Div([
        html.Div([
            html.H3("Acceleration (m/s^2)")
        ], className='Title'),
        html.Div([
            dcc.Graph(id='acceleration'),
        ], className='twelve columns acceleration'),
        dcc.Interval(id='acceleration-update', interval=1000, n_intervals=0),
    ], className='row acceleration-row')
], style={'padding': '0px 10px 15px 10px',
          'marginLeft': 'auto', 'marginRight': 'auto', "width": "900px",
          'boxShadow': '0px 0px 5px 5px rgba(204,204,204,0.4)'}
)
freq= 10
duration = 200 * freq
X = [0] * duration
Y = [0] * duration
Z = [0] * duration
Time = [0] * duration
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)


@app.callback(Output('acceleration', 'figure'), [Input('acceleration-update', 'n_intervals')])
def gen_wind_speed(interval):

    accel_x, accel_y, accel_z = sensor.accelerometer
    t = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    X.append(accel_x)
    Y.append(accel_y)
    Z.append(accel_z)
    Time.append(t)

    trace1 = Scatter(
	x=[Time],
        y=[X],
       # line=scatter.Line(
       #     color='#42C4F7'
        #),
        mode='lines',
	name='X'
    )

    trace2 = Scatter(
	x=[Time],
        y=[Y],
        #line= scatter.Line(
        #    color='#42C4F7'
        #),
        mode='lines',
	name='Y'
    )

    trace3 = Scatter(
	x=[Time],
        y=[Z],
        #line= scatter.Line(
        #    color='#42C4F7'
        #),
        mode='lines',
	name='Z'
    )

    layout = Layout(
        height=450,
        xaxis=dict(
            range=[0, 200],
            showgrid=False,
            showline=False,
            zeroline=False,
            fixedrange=True,
            tickvals=[0, 50, 100, 150, 200],
            ticktext=['200', '150', '100', '50', '0'],
            title='Time Elapsed (sec)'
        ),
        yaxis=dict(
            range=[min(0, min(X)),
                   max(20, max(X)+max(X))],
            showline=False,
            fixedrange=True,
            zeroline=False,
            nticks=6
        ),
        margin= lo.Margin(
            t=45,
            l=50,
            r=50
        ),
	transition=dict(
                duration=500,
                easing="cubic-in-out")
    )

    return Figure(data=[trace1, trace2, trace3], layout=layout)


if __name__ == '__main__':
#    app.run_server(debug=True)
    app.run_server(debug=True, host='127.0.0.1', port=5000)
