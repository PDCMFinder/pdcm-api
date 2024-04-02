#!/bin/sh
postgrest > /var/log/pdcm-api/postgrest.log 2>&1 &
nginx -g 'daemon off;' > /var/log/pdcm-api/web.log
