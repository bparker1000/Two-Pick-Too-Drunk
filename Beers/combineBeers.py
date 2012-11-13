import ujson


def read_beers(filename):
    fileinput = open(filename,'r')
    for line in fileinput:
        yield ujson.loads(line)



files = ['Beers_0_1000',
         'Beers_1001_2000',
         'Beers_2001_3000',
         'Beers_3001_4000',
         'Beers_4001_5000',
         'Beers_5001_6000',
         'Beers_6001_7000',
         'Beers_7001_8000',
         'Beers_8001_9000',
         'Beers_9001_10000',
         'Beers_10001_15000',
         'Beers_15001_20000',
         'Beers_20001_25000',
         'Beers_25001_30000',
         'Beers_30001_35000']

json = open('Beers.json','w')
for jsonDoc in files:
    reviews = read_beers(jsonDoc+'.json')
    for review in reviews:
        s = ujson.dumps(review)
        json.write(s+'\n')
json.close()

