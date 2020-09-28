# get-country-name

## dependencies for API and containerization
-> Python >= 3.3, Flask >= 0.12 and py-healthcheck

## dependencies for API containerization and Orchestration
-> Docker and Kubernetes

## Execution step to build docker image
docker build -t get-country-code:latest

## Execution step for Kubernetes deployment YAML

kubectl apply -f manifest.yaml

# Verify application endpoints

## Get country name by country code
curl http://0.0.0.0:8000/convert/Canada
curl http://0.0.0.0:8000/convert/India

## Check health of the application
curl http://localhost:8000/health

## Check diag of the api to see the response of application
curl http://localhost:8000/diag
