import collections
import utils
import settings
import re


def main():
    db = utils.connect_db('Two_Pick_Too_Drunk')
    beer_collection = db['beers']
    beer_collection.remove()
    
    beers = utils.read_beers()
    for beer in beers:
       doc = {'Brewery'   : beer['Brewery'],
              'BeerId'    : beer['BeerId'],
              'Name'      : beer['Name'],
              'BreweryId' : beer['BreweryId']
             }
       beer_collection.insert(doc)
    
if __name__=="__main__":
    main()
