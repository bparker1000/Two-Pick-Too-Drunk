import ujson
import unicodedata
import utils 
from reviewersorter import review_sorter



def main():
    db = utils.connect_db('Two_Pick_Too_Drunk')
    beer_collection = db['beers']

    ObannonsBeerList = ['2264' , #1.  Lagunitas Brown Sugar
                        '24651', #2.  Left Hand Polestar Pilsner
                        '1769' , #3.  Alaskan Smoked Porter
                        '73221', #4.  Rahr & Sons Visonary Brew
                        '1062' , #5.  Live Oak Hefe (5.2%)
                        '409'  , #6.  North Coast Scrimshaw (4.4%)
                        '2093' , #7.  Dogfish Head 90 Minute IPA (9%)
                        '1907' , #8.  Dos Equis (5%)
                        '2296' , #9.  Big Sky Moose Drool Brown Ale (4.2%)
                        '23720', #10. Real Ale Devils Backbone
                        '1212' , #11. Blue Moon (5.4%)
                        '1068' , #12. St. Arnold Christmas
                        '2508' , #13. Maredsous 8 (8%)
                        '75572', #14. Karbach Yule Shoot Your Eye Out
                                 #15. Anrey Orchard
                        '29602', #16. Smithwick's (4.5%)
                        '862'  , #17. Harp (5%)
                        '82128', #18. Real Ale B.A. Volume 15
                        '909'  , #19. Killian's Irish Red (4.9%)
                        '639'  , #20. New Castle (4.7%)
                        '412'  , #21. North Coast Old Rasputin
                        '754'  , #22. Guinness (4.1%)
                        '73'   , #23. Young's Double Choc. Stout (5.2%)
                        '49070', #24. Alaskan White (5.3%)
                        '3434' , #25. Left Hand Milk Stout NITRO (6%)
                        '78'   , #26. Blanche de Bruxelles
                        '1352' , #27. Shiner Bock (4.4%)
                        '72941', #28. Karbach Hopadillo
                                 #29. Live Oak Smoktoberfest
                        '33822', #30. Rahr Winter Warmer
                        '73576', #31. karbach Sympathy for the Lager
                        '72834', #32. Karbach Weiss Versa Wheat
                        '1946' , #33. Franziskaner Hefe-Weiss (5%)
                        '607'  , #34. Fat Tire (5.3%)
                        '1914' , #35. 1554 Enlightened Black Ale (5.5%)
                        '924'  , #36. Franziskaner Dunkel Weiss (5%)
                        '58017', #37. Batch 19
                        '666'  , #38. Hacker Pschorr WeisseDark
                        '102'  , #39. Sam Adams Octoberfest
                        '84831', #40. Ommegang Scythe & sickle
                        '2270' , #41. *Carlsberg 11.2oz (5%)
                        '48139', #42. *Oskar Blues Mama's Yella Pils (5.3%)
                                 #43. Woodchuck Winter
                        '25649', #44. *Pyramid Apricot (5.1%)
                        '27800', #45. Brknrdge Vanilla Porter
                        '86091', #46. Real Ale Black Quad
                        '61109', #47. *St. Arnold Weedwacker
                        '34804', #48. *Land Shark 4.7%)
                        '51480', #49. Brooklyn Sorachi Ace
                        '33'   , #50. Unibroue Maudite
                        '3295' , #51. Avery Old Jubilation
                        '1344' , #52. *St. Arnold Fancy Lawn Mower (4.9%)
                        '752'  , #53. *Guinness Foreign Extra Stout (7.5%)
                        '57286', #54. *Guinness Black Lager (4.5%)
                        '650'  , #55. *Guinness Extra Stout (6%)
                        '34'   , #56. *Unibrone La fin du monde
                        '246'  , #57. *Heineken (5%)
                        '403'  , #58. *North Coast ACME IPA
                        '14660', #59. Real Ale Coffee Porter
                        '63494', #60. *Lindeman's Pomme (4%)
                        '23713', #61. *Full Sail Sessions Lager (5.3%)
                        '50740', #62. *Full Sail Sessions Black (5.4%)
                        '53774', #63. *Sam Adams Stone Brook Red
                        '8951' , #64. *Stone Oaked Arrogant Bastard (7.2%)
                        '76781', #65. *Dogfish Positive Contact
                        '310'  , #66. Harpoon Winter Warmer
                        '45576', #67. Southern Star Bombshell Blonde (5.25%)
                        '71325', #68. Harpoon UFO Pumpkin
                        '689'  , #69. *Red Stripe (4.7%)
                        '9689' , #70. Avery White Rascal
                                 #71. *Strongbow Cider (5%)
                        '1768' , #72. Alaskan Winter 
                        '14712', #73. *Oskar Blues Old Chub Scottish Ale(6.5%)
                        '48933', #74. *Harpoon UFO White (4.8%)
                        '19956'] #75. *Rahr & Sons Blonde Lager (4.8%)
    
    print 'Sorting Obannon\'s reviews'
    reviews = utils.read_beers()
    obannonsReviews = list()
    obannonsDict = dict()
    json = open('Reviews/ObannonsData.json','w')
    for review in reviews:
        if review['BeerId'] in ObannonsBeerList:
            obannonsReviews.append(review)
            s = ujson.dumps(review)
            json.write(s+'\n')
    json.close()
    reviewersorter = review_sorter('obannons_reviews')
    reviewersorter.sort_reviews(obannonsReviews)

    for review in obannonsReviews:
        if review['BeerId'] in obannonsDict:
            obannonsDict[review['BeerId']].append(review['Reviewer'])
        else:
            obannonsDict[review['BeerId']] = [review['Reviewer']]

    print 'Reveiews per Obannons Beers'
    for beer in obannonsDict:
        Beer = beer_collection.find_one({"BeerId":beer})
        print 'Beer: '+Beer['Brewery']+ ' '+ Beer['Name'] + '\nNumber of reviews: '+str(len(obannonsDict[beer]))+'\n'
    


if __name__=="__main__":
    main()
