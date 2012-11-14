import collections
import utils
import settings
import re
import time

class review_sorter():

    def __init__(self,collection='reviewer'):
        self.db = utils.connect_db('Two_Pick_Too_Drunk')
        self.reviewer_collection = self.db[collection]
        self.reviewer_collection.remove()


    def sort_reviews(self,reviewsjson):
        self.reviews = reviewsjson
        self.count = 0
        self.count_unique = 0
        self.repeat = 0
        self.total_ratings = 0

        self.ReviewerDictionary = dict()

        for review in self.reviews:
            temp_person = review['Reviewer']
            temp_dic = review
        
            if temp_person in self.ReviewerDictionary:
                self.ReviewerDictionary[temp_person]['Ratings'].append({'BeerId':temp_dic['BeerId'],'Rating':temp_dic['rating']})
                self.total_ratings += float(temp_dic['rating'])
                self.repeat+=1
            else:
                self.count_unique += 1
                #temp_dic = review
                self.ReviewerDictionary[temp_person] = {'Ratings' : [{"BeerId": temp_dic['BeerId'], 
                                                           "Rating" : temp_dic['rating']}]}
                self.total_ratings += float(temp_dic['rating'])
            
            self.count+=1
      
        
        for Reviewer in self.ReviewerDictionary:
            doc = {"reviewer": Reviewer,
                   "Ratings":  self.ReviewerDictionary[Reviewer]['Ratings']
                  }
            self.reviewer_collection.insert(doc)

    
        print "Total lines ", self.count
        print "Repeated reviewers ", self.repeat
        print "Number of reviewers ",self.count_unique
        print "Average rating ", self.total_ratings/self.count
        print
        """ makeing stats """

        # 1 rating so lengeth = 3
        self.few_ratings=0
        # 2-5 ratings so length 4 - 7
        self.some_ratings = 0
        # < 5 so greater than 7
        self.lots_ratings = 0
    
    
        cursor = self.reviewer_collection.find()
        for d in cursor:
            doc_length =len(d['Ratings'])
            if doc_length == 1:
                self.few_ratings +=1
            elif doc_length < 6:
                self.some_ratings +=1
            else:
                self.lots_ratings +=1
            
        print "one rating", self.few_ratings
        print "2-5 ratings", self.some_ratings
        print " more than 5 ratings", self.lots_ratings
    

    
def main():
    reviews = utils.read_beers()
    sorter = review_sorter()
    sorter.sort_reviews(reviews)


if __name__=="__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print 'done with sorting after %.3f seconds'%(end_time-start_time)

