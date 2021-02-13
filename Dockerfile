FROM alpine:3.13.0 AS production

## Install dependencies
RUN apk update
RUN apk add nginx
RUN apk add screen
RUN apk add certbot certbot-nginx

# thanks to https://stackoverflow.com/questions/62554991/how-do-i-install-python-on-alpine-linux
# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install jinja2

## Prepare config files
RUN rm -R /etc/nginx/*

## Copy files to container
ADD nginx /etc/nginx/
RUN mkdir /etc/nginx/sites-available
RUN mkdir /etc/nginx/sites-enabled
ADD nsc /nsc
RUN chmod +x /nsc/nsc.py
ENV PATH="/nsc/bin:${PATH}"
RUN mkdir /nsc/bin
RUN ln -s /nsc/nsc.py /nsc/bin/nsc
COPY entrypoint.sh /etc/entrypoint.sh

RUN mkdir /html

RUN chmod +x /etc/entrypoint.sh
ENTRYPOINT /etc/entrypoint.sh