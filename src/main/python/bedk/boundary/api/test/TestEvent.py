'''
Created on Mar 4, 2014

@author: davidg
'''
import unittest
import random

from boundary.api.Event import Event

"""
Unit tests or boundary.api.Event.Event
"""
class Test(unittest.TestCase):


    def setUp(self):
        self.event = Event.getEvent()
        pass


    def tearDown(self):
        pass

    def testDefaults(self):
        e = Event(source='MySource',fingerprintFields='@title',title='MyTitle')
        self.assertEqual(e.severity,e.INFO,'Check default value of severity')
        self.assertEqual(e.organizationID,None,'Check default value of organizationID')
        self.assertEqual(e.sender,None,'Check default value of sender')
        self.assertEqual(e.properties,None,'Check default value of properties')
        
    def getRandomString(self):
        return str(random.random())
        
    def testOperationID(self):
        expectedOrganizationID = '3ehRi7uZeeaTN12dErF5XOnRXjC'
        self.event.organizationID = expectedOrganizationID
        self.assertEqual(self.event.organizationID,expectedOrganizationID)
        
    def testSeverity(self):
        expectedSeverity = Event.ERROR
        self.event.severity = expectedSeverity
        self.assertEqual(self.event.severity,expectedSeverity)
        
    def testSource(self):
        expectedSource = self.getRandomString()
        self.event.source = expectedSource
        self.assertEqual(self.event.source,expectedSource)
        
    def testSender(self):
        """
        """
        expectedSender = self.getRandomString()
        self.event.sender = expectedSender
        self.assertEqual(self.event.sender,expectedSender)
        
    def testFingerprintFields(self):
        expectedFingerprintFields = self.getRandomString()
        self.event.fingerprintFields = expectedFingerprintFields
        self.assertEqual(self.event.fingerprintFields,expectedFingerprintFields)
        
    def testTitle(self):
        expectedTitle = self.getRandomString()
        self.event.title = expectedTitle
        self.assertEqual(self.event.title,expectedTitle)



        
# TODO: Deal with this kind of error checking later   
#     def testMalformedOrganizationID(self):
#         self.assertR
#         with self.assertRaises(ValueError):
#             expectedOperationalID = 'DEADBEEF'
#             e = Event.getEvent()
#             e.operationalID = expectedOperationalID

        
    def testEventDefaults(self):
        expectedSource = 'Boundary Event API Testing'
        e = Event.getEvent()
        
        self.assertIsNone(e.organizationID)
        self.assertIsNone(e.title)
        self.assertEqual(e.source,expectedSource)
        





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()