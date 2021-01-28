FROM alpine:3.13.0

## Install dependencies
RUN apk update
RUN apk add nginx

## Prepare config files
RUN rm /etc/nginx/nginx.conf
RUN mkdir -p /run/nginx/

## Copy files to container
COPY nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT nginx && sh