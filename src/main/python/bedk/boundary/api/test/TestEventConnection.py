'''
Created on Mar 5, 2014

@author: davidg
'''
import unittest

from boundary.api.event import EventConnection
from boundary.api.event import Event
from boundary.api.test import TestEventAPI
import platform


class TestEventConnection(TestEventAPI):

    def setUp(self):
        self.organizationID = '3ehRi7uZeeaTN12dErF5XOnRXjC'
        self.apiKey = 'ARI0PzUzWYUo7GG1OxiHmABTpr9'
        self.apiHost = 'api.boundary.com'
        
    def tearDown(self):
        pass
    
    def testCreateEvent(self):
        # Create our Boundary Event Connection
        connection = EventConnection(self.apiKey,
                                     self.organizationID)
        event = Event.getDefaultEvent()
          
          
        #Send an event to the Boundary Server using the Boundary REST API
        eventID = connection.createEvent(event)
        self.assertIsNotNone(eventID,'Check for returned event ID')
         
    def testGetEvent(self):
        connection = EventConnection(self.apiKey,
                                     self.organizationID)
          
        event = connection.getEvent(213299714)
        print('event_type {0}, event: {1}'.format(type(event),event))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()