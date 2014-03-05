'''
Created on Mar 3, 2014

@author: davidg
'''
import json
# TODO: The original python 2.7.x module urllib2 feature set has been absorbed into urllib in python 3.x
import urllib
import base64

class EventConnection(object):
    '''
    Handles the interacation with the Boundary Server REST API.
    '''
    __DEFAULT_EVENT_PATH='events'
    def __init__(self,apiHost,apiKey,organizationID):
        '''
        Constructor
        '''
        self.__apiHost = apiHost
        self.__apiKey = apiKey
        self.__organizationID = organizationID
        # Generate our URI
        self.__buildURI()
        
    @property
    def apiHost(self):
        return self.__apiHost
    
    @apiHost.setter
    def apiHost(self,apiHost):
        self.__apiHost = apiHost
        # API host has changed rebuild the URI
        self.__uri = self.__buildURI()
    
    @property
    def apiKey(self):
        return self.__apiKey
    
    @property
    def organizationID(self):
        """
        This ends up being the default organization ID unless it
        is overidden by the organization ID in the event itself.
        """
        return self.__organizationID

    def __buildURI(self):
        """
        Generate the URI required for the REST call
        """
        #
        # Format the URI
        #
        uri = 'https://{0}/{1}/{2}'.format(self.__apiHost,self.__organizationID,self.__DEFAULT_EVENT_PATH)
        return uri
    
    def sendEvent(self,event):
        """
        sendEvent(self,event) -> String
        """
        return ''
    
    
        
        