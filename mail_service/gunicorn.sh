#!/bin/sh
gunicorn mail_service:app --log-file /app/gunicorn.log -w 2 --threads 8 -b 0.0.0.0:5000