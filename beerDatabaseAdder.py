import collections
import utils
import settings
import re


def main():
    db = utils.connect_db('Two_Pick_Too_Drunk')
    beer_collection = db['beers']
    beer_collection.remove()
    
    print 'Loading Beers'
    beers = utils.read_beers()
    brewery = []
    beersCount = 0
    for beer in beers:
        beersCount +=1
        if beer['Brewery'] not in brewery:
            brewery.append(beer['Brewery'])

        doc = {'Brewery'   : beer['Brewery'],
               'BeerId'    : beer['BeerId'],
               'Name'      : beer['Name'],
               'BreweryId' : beer['BreweryId']
              }
        beer_collection.insert(doc)
    print str(beersCount) + ' Beers over ' + str(len(brewery)) + ' Brewerys'


if __name__=="__main__":
    main()
