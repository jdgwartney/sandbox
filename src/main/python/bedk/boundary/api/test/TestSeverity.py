'''
Created on Mar 4, 2014

@author: davidg
'''
import unittest
from boundary.api.events import SEVERITY

class TestSeverity(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testEnumCount(self):
        self.assertTrue(len(list(SEVERITY)) == 4,'Check enumeration count')
    
    def testEnumMembers(self):
        pass
        
    def testEnumEquality(self):
        self.assertTrue(SEVERITY.CRITICAL == SEVERITY.CRITICAL, 'Check for equality')
        self.assertTrue(SEVERITY.ERROR == SEVERITY.ERROR, 'Check ERROR for equality')
        self.assertTrue(SEVERITY.INFO == SEVERITY.INFO, 'Check INFO for equality')
        self.assertTrue(SEVERITY.WARN == SEVERITY.WARN, 'Check WARN for equality')
        
    def testEnumSet(self):
        self.assertTrue(isinstance(SEVERITY.CRITICAL,SEVERITY))
        self.assertTrue(isinstance(SEVERITY.ERROR,SEVERITY))
        self.assertTrue(isinstance(SEVERITY.INFO,SEVERITY))
        self.assertTrue(isinstance(SEVERITY.WARN,SEVERITY))
    #
    # NOTE: PyDev highlights these as syntax errors but it is incorrect
    #
    def testEnumValues(self):
        self.assertEqual(str(SEVERITY.CRITICAL.value),'CRITICAL','Check CRITICAL string value')
        self.assertEqual(str(SEVERITY.ERROR.value),'ERROR','Check ERROR string value')
        self.assertEqual(str(SEVERITY.INFO.value),'INFO','Check INFO string value')
        self.assertEqual(str(SEVERITY.WARN.value),'WARN','Check WARN string value')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()