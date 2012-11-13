import ujson


def read_beers(filename):
    fileinput = open(filename,'r')
    for line in fileinput:
        yield ujson.loads(line)



files = ['Review_0_1000',
         'Review_1001_2000',
         'Review_2001_3000',
         'Review_3001_4000',
         'Review_4001_5000',
         'Review_5001_6000',
         'Review_6001_7000',
         'Review_7001_8000',
         'Review_8001_9000',
         'Review_9001_10000',
         'Review_10001_15000',
         'Review_15001_20000',
         'Review_20001_25000',
         'Review_25001_30000',
         'Review_30001_35000']

json = open('Reviews.json','w')
for jsonDoc in files:
    reviews = read_beers(jsonDoc+'.json')
    for review in reviews:
        s = ujson.dumps(review)
        json.write(s+'\n')
json.close()

