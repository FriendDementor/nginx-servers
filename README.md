# Minimal nginx configuration
With this config you have a simple nginx server running

## Run tests
```
docker build . -t production && docker build -f Dockerfile.test . -t test && docker run test
```
