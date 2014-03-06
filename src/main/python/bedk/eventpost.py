'''
Created on Mar 5, 2014

@author: davidg
'''

import requests
import json
import random
import platform

def getEvent():
    myMessage = str('test' + str(random.random()))
    myTitle = "Boundary API Event Test"
    myHost = platform.node()
    event = {"title": myTitle,
             "message": myMessage,
             "tags": ["example", "test", "stuff"],
             "fingerprintFields": ["@title"],
             "source": { "ref": myHost,"type": "host"}
            }

#     event = {
#     "title": "example",
#     "message": "test",
#     "tags": ["example", "test", "stuff"],
#     "fingerprintFields": ["@title"],
#     "source": {
#         "ref": "myhost",
#         "type": "host"
#             }
#     }
             
    return event 

# def printRequest(url,orgID,apiKey,event,headers):
#     print('url: {0}\norgID: {1}\napiKey: {2}\nevent: {3}\nheaders: {4}'.format(url,orgID,apiKey,event,headers))
# 
# def printResponse(statusCode,headers,text):
#     print('statusCode: {0}\nheaders: {1}\ntext: {2}'.format(statusCode,headers,text))
    


def main():
    apiKey = 'ARI0PzUzWYUo7GG1OxiHmABTpr9'
    orgID = '3ehRi7uZeeaTN12dErF5XOnRXjC'
    url = 'https://api.boundary.com/{0}/events'.format(orgID)
    event = getEvent()
#    auth = 'Basic ' + b64encode(('%s:%s' % ('', apiKey)).encode('utf-8')).strip().decode('utf-8')
    headers = {'Content-Type': 'application/json'}
    #printRequest(url,orgID,apiKey,event,headers)
    r = requests.post(url,data=json.dumps(event), headers=headers,auth=(apiKey,''))
#    printResponse(r.status_code,r.headers,r.json)
    # TODO: Defined constant for HTTP headers like location
    location = str(r.headers['Location'])
    # The HTTP Reponse header 'Location'
    eventID = location.split('/',6)[5]
    print(eventID)


    

if __name__ == '__main__':
    main()