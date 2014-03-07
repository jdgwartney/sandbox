'''
Created on Mar 5, 2014

@author: davidg
'''
import unittest

from boundary.api.event import EventConnection
from boundary.api.event import Event
from boundary.api.test import TestEventAPI


class TestEventConnection(TestEventAPI):


    def setUp(self):
        self.organizationID = '3ehRi7uZeeaTN12dErF5XOnRXjC'
        self.apiKey = 'ARI0PzUzWYUo7GG1OxiHmABTpr9'
        self.apiHost = 'api.boundary.com'
        self.source = 'Boundary Event API'
        self.fingerprintFields = '@title'
        self.title = 'Boundary API Event'

        self.myEvent = Event(self.source,
                        self.fingerprintFields,
                        self.title)

    def tearDown(self):
        pass
    
    def testSendEvent(self):
        # Create our Boundary Event Connection
        connection = EventConnection(self.apiKey,
                                     self.organizationID)
         
        #Send an event to the Boundary Server using the Boundary REST API
        eventID = connection.sendEvent(self.myEvent.getActiveFields())
        self.assertIsNotNone(eventID,'Check for returned event ID')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()