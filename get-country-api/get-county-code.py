import sys
import json
import requests
import urllib
import urllib.request as request
from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump
from http import HTTPStatus

api = Flask(__name__)
healthcheck = HealthCheck()
env_dump = EnvironmentDump()

@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def catch_all(path):
    # returns a 200 (not a 404) with the following contents:
    #return 'No Path found Please use right path\n'
	return 'Sorry there is no endpoint as such use these endpoints : /diag  :/convert/{country_name} :/health'

# Check api health for https://www.travel-advisory.info/api
@api.route('/diag')
def diagURL():
	api_status = requests.get('https://www.travel-advisory.info/api')
	if(api_status.status_code==200):
		return api_status.reason
	else:
		return 'Error:  Failed to fetch data from API. Please check API is working or not'

# return health of the service
def application_status():
	fetchApiResponse()
	client = getCountryCode('Canada')
	return True, "Application is Healthy"

# route to health for application
api.add_url_rule("/health", "healthcheck", view_func=lambda: healthcheck.run())
healthcheck.add_check(application_status)

# Fetch country code based on country name
@api.route('/convert/<code>')
def CountryCode(code):
	fetchApiResponse()
	result = getCountryCode(code)
	if(result):
		return result
	else:
		return 'Please enter valid code'


def fetchApiResponse():
	countryCode = {}
	with request.urlopen('https://www.travel-advisory.info/api') as data:
		if(data.getcode()==200):
			source = data.read()
			jsondata = json.loads(source)
			for item in jsondata['data'].keys(): ## Filter country code and name and country name fields only
				countryName = jsondata['data'][item]['name']
				countryCode[countryName] = item
			with open('data.json', 'w') as f: ## Save jsondata in data.json file
				json.dump(countryCode, f, indent = 5, sort_keys = True)
		else:
			print('Error:  Failed to fetchdata from API. Please use the working API')

## Parse data.json file to filter data by country name and return country code
def getCountryCode(country):
	with open('data.json', 'r') as content:
		data = json.load(content)
		if country in data:
			result = data[country]
		else:
			result = 'Country code not found in the given list.'
		return result

if __name__ == '__main__':
	api.run(debug=True,host='0.0.0.0')
