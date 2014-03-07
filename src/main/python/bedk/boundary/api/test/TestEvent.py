'''
Created on Mar 4, 2014

@author: davidg
'''
import unittest


from boundary.api.event import Event
from boundary.api.test import TestEventAPI

"""
Unit tests or boundary.api.Event.Event
"""
class TestEvent(TestEventAPI):


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
                
    def testOrganizationID(self):
        expectedOrganizationID = '3ehRi7uZeeaTN12dErF5XOnRXjC'
        self.event.organizationID = expectedOrganizationID
        self.assertEqual(self.event.organizationID,expectedOrganizationID,'Check organizationID')
        
    def testSeverity(self):
        expectedSeverity = Event.ERROR
        self.event.severity = expectedSeverity
        self.assertEqual(self.event.severity,expectedSeverity,'Check severity')
        
    def testSource(self):
        expectedSource = self.getRandomString()
        self.event.source = expectedSource
        self.assertEqual(self.event.source,expectedSource,'Check source')
        
    def testSender(self):
        expectedSender = self.getRandomString()
        self.event.sender = expectedSender
        self.assertEqual(self.event.sender,expectedSender,'Check sender')
        
    def testFingerprintFields(self):
        expectedFingerprintFields = self.getRandomString()
        self.event.fingerprintFields = expectedFingerprintFields
        self.assertEqual(self.event.fingerprintFields,expectedFingerprintFields,'Check fingerprintFields')
        
    def testTagsString(self):
        expectedTags = self.getRandomString()
        self.event.tags = expectedTags
        self.assertEqual(self.event.tags,expectedTags,'Check tags')
        
    def testTagsArray(self):
        tags = ['red','green','blue']
        self.event.tags = tags
        self.assertEqual(self.event.tags,tags,'Check tags array')
        
    def testTitle(self):
        expectedTitle = self.getRandomString()
        self.event.title = expectedTitle
        self.assertEqual(self.event.title,expectedTitle,'Check title')
        
    def testMessage(self):
        expectedMessage = self.getRandomString()
        self.event.message = expectedMessage
        self.assertEqual(self.event.message,expectedMessage,'Check message')
        
    def testCreatedAt(self):
        expectedCreatedAt = self.getRandomString()
        self.event.createdAt = expectedCreatedAt
        self.assertEqual(self.event.createdAt,expectedCreatedAt,'Check createdAt')

    def testReceivedAt(self):
        expectedReceivedAt = self.getRandomString()
        self.event.receivedAt = expectedReceivedAt
        self.assertEqual(self.event.receivedAt,expectedReceivedAt,'Check receivedAt')

    def testEventId(self):
        expectedEventId = self.getRandomString()
        self.event.eventId = expectedEventId
        self.assertEqual(self.event.eventId,expectedEventId,'Check evenId')


        
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