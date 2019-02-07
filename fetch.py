import urllib2
import json

# http://www.omdbapi.com/?t=MovieName&apikey=31f9c50


def movieSearch(query):
    key = '31f9c50'

    url = urllib2.urlopen('http://www.omdbapi.com/?t=' + str(query) + '&apikey=' + str(key))
    data = json.load(url)

    print(data['Title'])
    print(data['Year'])
    print(data['Released'])
    print(data['Director'])
    print(data['Website'])
    print(data['Production'])
    print(data['imdbRating'])

def reSearch():

    print('\n')
    print("Do you wanna search another movie?")

    x = raw_input("Y/N ? =>")
    if(x == 'Y' or x == 'y'):
        y = raw_input("Enter Movie:")
        movieSearch(y)
        reSearch()

    else:
        quit()



if __name__ == "__main__":

    InputMovie = raw_input("Enter Movie Name:")

    movieSearch(InputMovie)
    reSearch()





















