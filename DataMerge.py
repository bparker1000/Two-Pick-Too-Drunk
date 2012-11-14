import ujson
import unicodedata

def read_json(filename):
    fileinput = open(filename,'r')
    for line in fileinput:
        yield ujson.loads(line)

beers = read_json('Beers/Beers.json')
reviews = read_json('Reviews/Reviews.json')

BeerDict = dict()
ReviewList = list()


for beer in beers:
    BeerDict[beer['BeerId']] = {'BreweryId': beer['BreweryId'],'Name':beer['Name'],'Brewery':beer['Brewery']}

json = open('Data.json','w')
for review in reviews:
    review.update(BeerDict[review['BeerId']])
    s = ujson.dumps(review)
    json.write(s+'\n')
json.close()


