# get-country-name

## dependencies for script execution
-> Python 3.3

## dependencies for service and containerization
-> Python >= 3.3, Flask >= 0.12 and py-healthcheck

## dependencies for service containerization and Orchestration
-> docker and Kubernetes

## Execution steps for one countryCode
ranjitkumargollamudi@Ranjits-MacBook-Pro get-country-name % python3 fetch-country-name.py Au
Country name for country code AU is Australia

## Execution steps for multiple countryCodes

ranjitkumargollamudi@Ranjits-MacBook-Pro get-country-name % python3 fetch-country-name.py Au aM IN LR usa
Country name for country code AU is Australia
Country name for country code AM is Armenia
Country name for country code IN is India
Country name for country code LR is Liberia
Country code USA was not found. Please pass valid country code

## Get country name application
https://github.com/ranjitkumar518/get-country-name/tree/master/fetch-country-api
