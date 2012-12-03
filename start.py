import json
import os
from pymongo import Connection
import time
import datetime

class DataImporter:
    
    def saveJson(self, path):
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith(".json"):
                    subFolder = root[17:root.find("_json")]
                    dbName = name.replace(".json","")
                    self.mongo(subFolder,dbName,root+'/'+name)


    def mongo(self, subFolder, name, json):
        connection = Connection()
        db = connection.Hackathon
        collection = db[name]
        print json
        for entry in self.load_json(json):
            entry['SubFolder'] = subFolder
            if name == 'posts':
                if entry['ViewCount'] == '':
                    entry['ViewCount'] = '0'

                if 'ViewCount' in entry.keys():
                    entry['ViewCount'] = int(entry['ViewCount'])

                if 'LastEditorUserId' in entry.keys():
                    entry['LastEditorUserId'] = int(entry['LastEditorUserId'])

                if 'LastActivityDate' in entry.keys():
                    entry['LastActivityDate'] = datetime.datetime(*time.strptime(entry['LastActivityDate'],'%Y-%m-%dT%H:%M:%S.%f')[0:6])
                
                if 'LastEditDate' in entry.keys():
                    entry['LastEditDate'] = datetime.datetime(*time.strptime(entry['LastEditDate'],'%Y-%m-%dT%H:%M:%S.%f')[0:6])
                if 'CommentCount' in entry.keys():
                    entry['CommentCount'] = int(entry['CommentCount'])
                
                if 'AnswerCount' in entry.keys():
                    entry['AnswerCount'] = int(entry['AnswerCount'])
                
                if 'AcceptedAnswerId' in entry.keys():
                    entry['AcceptedAnswerId'] = int(entry['AcceptedAnswerId'])
                
                if 'Score' in entry.keys():
                    entry['Score'] = int(entry['Score'])
                
                if 'CommunityOwnedDate' in entry.keys():
                    entry['CommunityOwnedDate'] =datetime.datetime(*time.strptime(entry['CommunityOwnedDate'],'%Y-%m-%dT%H:%M:%S.%f')[0:6])
                
                if 'PostTypeId' in entry.keys():
                    entry['PostTypeId'] = int(entry['PostTypeId'])
                
                if 'OwnerUserId' in entry.keys():
                    entry['OwnerUserId'] = int(entry['OwnerUserId'])
                
                if 'CreationDate' in entry.keys():
                    entry['CreationDate'] = datetime.datetime(*time.strptime(entry['CreationDate'],'%Y-%m-%dT%H:%M:%S.%f')[0:6])
                
                if 'FavoriteCount' in entry.keys():
                    entry['FavoriteCount'] = int(entry['FavoriteCount'])

            elif name == 'users':
                entry['Views'] = int(entry['Views'])
                entry['DownVotes'] = int(entry['DownVotes'])
                entry['LastAccessDate'] = datetime.datetime(*time.strptime(entry['LastAccessDate'],'%Y-%m-%dT%H:%M:%S.%f')[0:6])
                entry['Reputation'] = int(entry['Reputation'])
                entry['UpVotes'] = int(entry['UpVotes'])
                entry['CreationDate'] = datetime.datetime(*time.strptime(entry['CreationDate'],'%Y-%m-%dT%H:%M:%S.%f')[0:6])
            collection.insert(entry)

    def load_json(self, path):
    # open a file and return it as json
        with(open(path)) as f:
            for line in f:
                try:
                    yield json.loads(line)
                except:
                    pass

