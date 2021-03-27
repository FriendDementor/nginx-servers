# NSC Nginx Simple Client

A short list of commands to have a simple server of nginx

## Run tests
```
docker build . -t production && docker build -f Dockerfile.test . -t test && docker run test
```

## Production deploy
```
docker run -p 80:80 --name nsc -it -d production
```

