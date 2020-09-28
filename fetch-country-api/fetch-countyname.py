import sys
import json
import requests
import urllib
import urllib.request as request
from flask import Flask
from http import HTTPStatus

api = Flask(__name__)

@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def catch_all(path):
    # returns a 200 (not a 404) with the following contents:
    #return 'No Path found Please use right path\n'
	return 'Sorry there is no endpoint as such use these endpoints : /getcountryname/{country_code} :/healthcheck'

# Check api health for https://www.travel-advisory.info/api
@api.route('/healthcheck')
def callURL():
	api_status = requests.get('https://www.travel-advisory.info/api')
	if(api_status.status_code==200):
		return api_status.reason
	else:
		return 'Error:  Failed to fetch data from API. Please check API is working or not'

# Fetch country name based on country code
@api.route('/getcountryname/<code>')
def CountryName(code):
	fetchApiResponse()
	result = getCountryName(code)
	if(result):
		return result
	else:
		return 'Please enter valid code'


def fetchApiResponse():
	countryName = {}
	with request.urlopen('https://www.travel-advisory.info/api') as data:
		if(data.getcode()==200):
			source = data.read()
			jsondata = json.loads(source)
			for item in jsondata['data'].keys(): ## Filter country code and name and country name fields only
				countryName[item] = jsondata['data'][item]['name']
			with open('data.json', 'w') as f: ## Save jsondata in data.json file
				json.dump(countryName, f, indent = 5, sort_keys = True)
		else:
			print('Error:  Failed to fetchdata from API. Please use the working API')

## Parse data.json file to filter data by country code and return country name
def getCountryName(country):
	with open('data.json', 'r') as content:
		data = json.load(content)
		# for country in countries:
		country = country.upper() ## To convert user input to upper case
		if country in data:
			result = data[country]
			# print('Country name for country code ' + country + ' is '  + data[country])
		else:
			result = 'Country code not found in the given list.'
			# print('Country code '+ country +' was not found. Please pass valid country code')
		return result

if __name__ == '__main__':
	api.run(debug=True,host='0.0.0.0')
