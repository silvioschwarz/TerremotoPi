#! /bin/python3

import dash_table
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
from flask import Flask

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.graph_objs.layout as lo
from flask import Flask
import numpy as np
import pandas as pd
import os
import sqlite3
import datetime as dt

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
        dcc.Interval(id='acceleration-update', interval=500, n_intervals=0),
    ], className='row acceleration-row')
], style={'padding': '0px 10px 15px 10px',
          'marginLeft': 'auto', 'marginRight': 'auto', "width": "900px",
          'boxShadow': '0px 0px 5px 5px rgba(204,204,204,0.4)'}
)


@app.callback(Output('acceleration', 'figure'), [Input('acceleration-update', 'n_intervals')])
def gen_wind_speed(interval):
    now = dt.datetime.now()
    sec = now.second
    minute = now.minute
    hour = now.hour
    #microsecond = now.microsecond

    total_time = (hour * 3600) + (minute * 60) + (sec)# + (microsecond)

    con = sqlite3.connect("./data/acceleration-data.db")
    df = pd.read_sql_query('SELECT Time, X, Y, Z from acceleration where\
                            rowid > "{}" AND rowid <= "{}";'
                            .format(total_time-200, total_time), con)

    trace1 = Scatter(
	#x=df['Time'],
        y=df['X'],
       # line=scatter.Line(
       #     color='#42C4F7'
        #),
        mode='lines',
	name='X'
    )

    trace2 = Scatter(
	#x=df['Time'],
        y=df['Y'],
        #line= scatter.Line(
        #    color='#42C4F7'
        #),
        mode='lines',
	name='Y'
    )

    trace3 = Scatter(
	#x=df['Time'],
        y=df['Z'],
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
            range=[min(0, min(df['X'])),
                   max(20, max(df['X'])+max(df['X']))],
            showline=False,
            fixedrange=True,
            zeroline=False,
            nticks=max(6, round(df['Z'].iloc[-1]/10))
        ),
        margin= lo.Margin(
            t=45,
            l=50,
            r=50
        )#,
	#transition=dict(
        #        duration=200,
        #        easing="cubic-in-out")
    )

    return Figure(data=[trace1, trace2, trace3], layout=layout)


if __name__ == '__main__':
    app.run_server(debug=True)
#    app.run_server(debug=True, host='127.0.0.1', port=5000)
