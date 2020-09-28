import sys
import json
import urllib.request as request

def main(*countries):
	fetchApiResponse()
	getCountryName(*countries)

## Fetch response from api and store in data.json file
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
def getCountryName(*countries):
	with open('data.json', 'r') as content:
		data = json.load(content)
		for country in countries[0]:
			country = country.upper() ## To convert user input to upper case
			if country in data:
				print('Country name for country code ' + country + ' is '  + data[country])
			else:
				print('Country code '+ country +' was not found. Please pass valid country code')

if __name__=='__main__':
    main(sys.argv[1:])
