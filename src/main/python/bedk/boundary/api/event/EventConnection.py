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
import http.client

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
        self.__createEventHeaders = {'Content-Type': 'application/json'}
        self.__getEventHeaders = {'Accept': 'application/json'}
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

    def createEvent(self,event):
        """
        sendEvent(self,event) -> String
        """
        
        #
        # Extract fields that have been set
        #
        e = event.getActiveFields()

        #
        # TODO: What kind of errors can this through?? Add handling for errors
        #
        r = requests.post(self.__uri,data=json.dumps(e), headers=self.__createEventHeaders,auth=self.__authorization)
        
        if r.status_code == http.client.CREATED:
            # TODO: Defined constant for HTTP headers like location
            # The HTTP Response header 'Location'
            locationHeader = str(r.headers['Location'])
            eventId = int(locationHeader.split('/',6)[5])
        else:
            print('HTTP Status Code: ' + str(r.status_code))
            eventId = None

        return eventId
    
    def getEvent(self,eventId):
        """
        """
        # TODO: checks to ensure event ID is a number
        uri = self.__uri + '/' + str(eventId)
        print('uri: ' + uri)
        
        r = requests.get(uri,headers=self.__getEventHeaders, auth=self.__authorization)
        print('HTTP Status Code: ' + str(r.status_code))
        print(r.text)
        e = json.loads(r.text)
        return Event.toEvent(e)


    
        
        