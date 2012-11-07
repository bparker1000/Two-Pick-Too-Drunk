import urllib
import re


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

x=1
brewBeerDict = dict()
while x<10:
    f = urllib.urlopen("http://beeradvocate.com/beer/profile/"+str(x)+"/")
    s = f.read()
    f.close()
    title = s[s.find("<title>")+len("<title>"):s.find("-",s.find("<title>"))]
    print title
    if title.find('404 Not Found')<0:
        beerNames = list()
        beers = find_list_of_beers(x,s)
        for beer in beers:
            f = urllib.urlopen("http://beeradvocate.com/beer/profile/"+str(x)+"/"+beer)
            s = f.read()
            f.close()
            beerName = s[s.find("<title>")+len("<title>"):s.find("- "+title,s.find("<title>"))]
            beerNames.append(beerName)
        brewBeerDict[title] = beerNames
    x+=1

print brewBeerDict
