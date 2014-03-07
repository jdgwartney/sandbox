'''
Created on Mar 6, 2014

@author: davidg
'''
import unittest
import random


class TestEventAPI(unittest.TestCase):
    
    def getRandomString(self):
        return str(random.random())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()