#!/bin/bash
echo "Starting gunicorn web server ..."
gunicorn --bind=0.0.0.0:8000 --timeout 600 application:app -w 4
# python2 /code/application.py