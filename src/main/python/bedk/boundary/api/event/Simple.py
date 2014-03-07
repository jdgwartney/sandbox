'''
Created on Mar 6, 2014

@author: davidg
'''

from boundary.api.event import EventConnection
from boundary.api.event import Event

def createEvent():
    org = '3ehRi7uZeeaTN12dErF5XOnRXjC'
    key = 'ARI0PzUzWYUo7GG1OxiHmABTpr9'

    c = EventConnection(apiKey=key,organizationID=org)
    
    e = Event.getEvent()
    e.severity = Event.CRITICAL
    
    print(c.sendEvent(e))
    

__all__ = ['createEvent']

if __name__ == '__main__':
    createEvent()



