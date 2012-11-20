import urllib
import re
import ujson
import sys


def read_beers(filename):
    fileinput = open(filename,'r')
    for line in fileinput:
        yield ujson.loads(line)

def remove_html_tags(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)

def remove_extra_spaces(data):
    p = re.compile(r'\s+')
    return p.sub(' ', data)

def find_list_of_beers(data,json,beerId):
    ratingPattern = re.compile(r'<span class=\"BAscore_norm\">\d+\.\d*</span>')
    reviewPattern = re.compile(r'<b>([A-Za-z0-9\-\_]+)</b></a></h6>')
    reviewers = re.findall(reviewPattern,data)
    ratings = re.findall(ratingPattern, data)
    for x in ratings:
        rating = x.replace('<span class=\"BAscore_norm\">','')
        rating = rating.replace('</span>','')
        reviewer = reviewers[ratings.index(x)].replace('<b>','').replace('</b></a></h6>','')
        beerDump = {"BeerId":beerId, "Reviewer":reviewer,"rating":rating}
        s = ujson.dumps(beerDump)
        json.write(s+'\n')



start = sys.argv[1]
stop = sys.argv[2]
json = open('../Reviews/Review_'+start+'_'+stop+'.json','w')
beers = read_beers('../Beers/Beers_'+start+'_'+stop+'.json')
for beer in beers:
    print beer['Name']
    for reviews in ['0','10','20','30','40','50','60','70','80','90']:
        f = urllib.urlopen("http://beeradvocate.com/beer/profile/"+str(beer['BreweryId'])+"/"+str(beer['BeerId'])+"/?sort=topr&start="+reviews)
        s = f.read()
        f.close()
        find_list_of_beers(s,json,beer['BeerId'])
json.close()        

