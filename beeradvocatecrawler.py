import urllib
import re
import ujson


def remove_html_tags(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)

def remove_extra_spaces(data):
    p = re.compile(r'\s+')
    return p.sub(' ', data)

def find_list_of_beers(brewery, data):
    p = re.compile(r'href=[\'"]/beer/profile/'+str(brewery)+'/\d+[0-9]')
    result = re.findall(p, data)
    returnResults = list()
    for x in result:
        beer = x.replace("href=\"/beer/profile/"+str(brewery)+"/",'')
        if beer not in returnResults:
            returnResults.append(beer)
    return returnResults

json = open('Beers.json','w')
x=1
while x<10:  #30260 is the full list
    f = urllib.urlopen("http://beeradvocate.com/beer/profile/"+str(x)+"/?view=beers&show=all")
    s = f.read()
    f.close()
    title = s[s.find("<title>")+len("<title>"):s.find("-",s.find("<title>"))]
    print str(x) +' ' + title
    if title.find('404 Not Found')<0:
        beerNames = list()
        beers = find_list_of_beers(x,s)
        for beer in beers:
            f = urllib.urlopen("http://beeradvocate.com/beer/profile/"+str(x)+"/"+beer)
            s = f.read()
            f.close()
            beerName = s[s.find("<title>")+len("<title>"):s.find("- "+title,s.find("<title>"))]
            BeerDump = {"BeerId":beer,"Name":beerName,"Brewery":title,"BreweryId":x}
            s = ujson.dumps(BeerDump)
            json.write(s+'\n')

    x+=1
json.close()
