# get-country-name

## dependencies for API and containerization
-> Python >= 3.3, Flask >= 0.12 and py-healthcheck

## dependencies for API containerization and Orchestration
-> Docker and Kubernetes

## Execution step to build docker image
docker build -t get-country-name:latest

## Execution step for Kubernetes deployment YAML

kubectl apply -f manifest.yaml

# Verify application endpoints

## Get country name by country code
curl http://localhost:8000/getcountryname/US

## Check health of the application
curl http://localhost:8000/healthcheck
