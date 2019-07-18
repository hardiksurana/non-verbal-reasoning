#!/bin/sh
gunicorn --config ./app/src/gunicorn_conf.py application:app