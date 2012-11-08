import urllib
import re
import ujson


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
    reviewPattern = re.compile(r'<b>\w+</b>')
    reviewers = re.findall(reviewPattern,data)
    ratings = re.findall(ratingPattern, data)
    reviewers.remove('<b>Beers</b>')
    reviewers.remove('<b>Events</b>')
    try:
        reviewers.remove('<b>average</b>')
        reviewers.remove('<b>average</b>')
    except:
        pass
    for x in ratings:
        rating = x.replace('<span class=\"BAscore_norm\">','')
        rating = rating.replace('</span>','')
        reviewer = reviewers[ratings.index(x)].replace('<b>','').replace('</b>','')
        beerDump = {"BeerId":beerId, "Reviewer":reviewer,"rating":rating}
        s = ujson.dumps(beerDump)
        json.write(s+'\n')


json = open('Review_0_1000.json','w')
beers = read_beers("Beers_0_1000.json")
for beer in beers:
    print beer['Name']
    for reviews in ['0','10','20','30','40','50','60','70','80','90']:
        f = urllib.urlopen("http://beeradvocate.com/beer/profile/"+str(beer['BreweryId'])+"/"+str(beer['BeerId'])+"/?sort=topr&start="+reviews)
        s = f.read()
        f.close()
        find_list_of_beers(s,json,beer['BeerId'])
json.close()        

