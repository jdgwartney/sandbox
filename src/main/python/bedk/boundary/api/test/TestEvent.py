'''
Created on Mar 4, 2014

@author: davidg
'''
import unittest

from boundary.api.event import Event

"""
Unit tests or boundary.api.event.Event
"""
class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testDefaults(self):
        e = Event(source='MySource',fingerprintFields='@title',title='MyTitle')
        self.assertEqual(e.severity,e.INFO,'Check default value of severity')
        self.assertEqual(e.organizationID,None,'Check default value of organizationID')
        self.assertEqual(e.sender,None,'Check default value of sender')
        self.assertEqual(e.properties,None,'Check default value of properties')

        
    def testSetSeverity(self):
        pass





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()