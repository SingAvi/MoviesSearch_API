import urllib2
import json

InputMovie = input("Enter Movie Name: ")

def movieSearch(query):
    key = '31f9c50'

    url = urllib2.urlopen('http://www.omdbapi.com/?t=' + query + '&apikey=' + key)
    data = json.load(url)

    print(data['Title'])
    print(data['Year'])



movieSearch(InputMovie)










