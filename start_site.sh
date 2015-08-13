#!/bin/bash

set -e
LOGFILE=/root/proweb/website/site.log
LOGDIR=$(dirname $LOGFILE)

NUM_WORKERS=3

USER=root
GROUP=root

cd /root/proweb/website/
source ../bin/activate/

test -d $LOGDIR || mkdir -p $LOGDIR


exec gunicorn -w $NUM_WORKERS -b 0.0.0.0:8000 website.wsgi:application --user=$USER --group=$GROUP