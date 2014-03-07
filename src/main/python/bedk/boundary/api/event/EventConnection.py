"""
Created on Mar 3, 2014

@author: davidg
"""


import requests
from requests.auth import HTTPBasicAuth
import json
import platform
from datetime import datetime
from boundary.api.event import Event

class EventConnection(object):
    '''
    Handles the interaction with the Boundary Server REST API.
    '''
    
    # Default API host if none is specified
    __DEFAULT_API_HOST='api.boundary.com'
    
    # Define our event path for the REST calls
    __DEFAULT_EVENT_PATH='events'
    def __init__(self,apiKey,organizationID,apiHost=__DEFAULT_API_HOST):
        '''
        Constructor
        '''
        self.__apiHost = apiHost
        self.__apiKey = apiKey
        self.__organizationID = organizationID
        # Generate our URI
        self.__headers = {'Content-Type': 'application/json'}
        self.__authorization = HTTPBasicAuth(self.__apiKey, '')
        self.__uri = 'https://{0}/{1}/{2}'.format(self.__apiHost,self.__organizationID,self.__DEFAULT_EVENT_PATH)

        
    @property
    def apiHost(self):
        return self.__apiHost
        
    @property
    def apiKey(self):
        return self.__apiKey
    
    @property
    def organizationID(self):
        """
        This ends up being the default organization ID unless it
        is overridden by the organization ID in the event itself.
        """
        return self.__organizationID

    
    def getEvent(self):
        myMessage = str('test @' + str(datetime.now()))
        myTitle = "Boundary API Event Test"
        myHost = platform.node()
        event = {"title": myTitle,
                 "message": myMessage,
                 "tags": ["example", "test", "stuff"],
                 "fingerprintFields": ["@message"],
                 "source": { "ref": myHost,"type": "host"}
                 }
        return event

    def sendEvent(self,event):
        """
        sendEvent(self,event) -> String
        
        
        """
        event = self.getEvent()
        

        #
        # TODO: What kind of errors can this through??
        r = requests.post(self.__uri,data=json.dumps(event), headers=self.__headers,auth=self.__authorization)
        # TODO: Defined constant for HTTP headers like location
        # The HTTP Response header 'Location'
        location = str(r.headers['Location'])
        eventID = location.split('/',6)[5]

        return eventID
    
def dumpDict(e):
    for f in e.keys():
        print('key: {0}, key_type: {1}, value: {2}, type: {3}'.format(f,type(f),e[f],type(e[f])))
    
def debug():
    c = EventConnection('foo','bar')
    d = c.getEvent()
    event = Event.getEvent()
    
    dumpDict(event.getActiveFields())
    
#     dumpDict(d)
#     print(json.dumps(d))
    
if __name__ == '__main__':
    debug()
    
    
        
        