#!/bin/sh
postgrest &
nginx -g 'daemon off;' 