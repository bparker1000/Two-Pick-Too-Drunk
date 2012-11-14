import ujson
import unicodedata

def read_beers(filename):
    fileinput = open(filename,'r')
    for line in fileinput:
        yield ujson.loads(line)

reviews = read_beers('Reviews.json')

ReviewsDict = dict()

for review in reviews:
    if review['Reviewer'] not in ReviewsDict.keys():
        ReviewsDict[review['Reviewer']] = [{'beer':review['BeerId'],'rating':float(review['rating'])}]
    else:
        newDict= {'beer':review['BeerId'],'rating':float(review['rating'])}
        if newDict not in ReviewsDict[review['Reviewer']]:
            ReviewsDict[review['Reviewer']].append(newDict)


output_file = open("ReviewData.xls",'w')
output_file.write('Reviews\tNumber Of Reivew\tAverage Ranking\n')
print 'makingfile'
for reviewer in ReviewsDict:
    count  = len(ReviewsDict[reviewer])
    average_rating = 0.0
    for review in ReviewsDict[reviewer]:
        average_rating += review['rating']
    average_rating = average_rating/float(count)
    output_file.write(reviewer+'\t'+str(count)+'\t'+str(round(average_rating,2))+'\n')
output_file.close()

