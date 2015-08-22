#!/bin/bash

set -e
LOGFILE=/root/proweb/website/site.log
LOGDIR=$(dirname $LOGFILE)

NUM_WORKERS=3

USER=root
GROUP=root

cd /root/proweb/website/
source ../bin/activate

test -d $LOGDIR || mkdir -p $LOGDIR


exec gunicorn -w $NUM_WORKERS -b 127.0.0.1:8080 website.wsgi:application --user=$USER --group=$GROUP