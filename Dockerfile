FROM alpine:3.13.0

## Install dependencies
RUN apk update
RUN apk add nginx
RUN apk add npm
RUN apk add nodejs
RUN apk add screen

## Prepare config files
RUN rm /etc/nginx/nginx.conf
RUN mkdir -p /run/nginx/

## Copy files to container
COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /etc/entrypoint.sh
RUN chmod +x /etc/entrypoint.sh
COPY src /srv

ENTRYPOINT /etc/entrypoint.sh