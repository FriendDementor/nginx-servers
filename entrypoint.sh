#!/bin/sh

# Start nginx
screen -S nginx -d -m nginx

# Adding cron tab task for ssl renew
crontab -l | { cat; echo "0	12	*	*	*	/usr/bin/certbot renew --quiet"; } | crontab -

# 

# Do not close the container
sh

