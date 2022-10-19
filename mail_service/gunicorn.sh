#!/bin/sh
gunicorn mail_service:app -w 2 --threads 8 -b 0.0.0.0:80