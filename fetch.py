import urllib2
import json

api_key = '31f9c50'

url = urllib2.urlopen('http://www.omdbapi.com/?t=James&y=1996&plot=full&apikey=31f9c50')

readableFormat = json.load(url)

print(readableFormat)
