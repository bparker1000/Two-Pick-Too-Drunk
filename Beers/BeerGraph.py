import ujson
import unicodedata

def read_beers(filename):
    fileinput = open(filename,'r')
    for line in fileinput:
        yield ujson.loads(line)


beers = read_beers('Beers.json')

BreweryToId = dict()
beerCount = dict()

for beer in beers:
    if beer['BreweryId'] not in BreweryToId.keys():
        BreweryToId[beer['BreweryId']] = beer['Brewery']
    if beer['BreweryId'] not in beerCount.keys():
        beerCount[beer['BreweryId']] = [beer['BeerId']]
    else:
        beerList = beerCount[beer['BreweryId']]
        beerList.append(beer['BeerId'])
        beerCount[beer['BreweryId']] = beerList


output_file = open("BeerData.xls",'w')
output_file.write('Brewery\tCount\n')
print 'makingfile'
for brewery in beerCount:
    breweryName = unicodedata.normalize('NFKD', BreweryToId[brewery]).encode('ascii','ignore')
    output_file.write(breweryName+'\t'+str(len(beerCount[brewery]))+'\n')
output_file.close()
