#!/bin/sh

# Start node server
screen -S nodejs -d -m node /srv/nodejs/server.js

# Start nginx
screen -S nginx -d -m nginx

# Do not close the container
sh

