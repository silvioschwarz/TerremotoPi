#! /bin/sh
gunicorn -c gunicorn.conf -b 0.0.0.0:5000 app:server
