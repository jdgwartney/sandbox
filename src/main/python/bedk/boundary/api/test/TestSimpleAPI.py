'''
Created on Mar 10, 2014

@author: davidg
'''
import unittest
from boundary.api.event import createEvent


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCreateEvent(self):
        organizationID = '3ehRi7uZeeaTN12dErF5XOnRXjC'
        apiKey = 'ARI0PzUzWYUo7GG1OxiHmABTpr9'
        apiHost = 'api.boundary.com'

        eventID = createEvent(apiHost,apiKey,'@title','Testing createEvent()',organizationID)


    def testGetEvent(self):
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()