'''
Created on Mar 6, 2014

@author: davidg
'''
import platform

from boundary.api.event import EventConnection
from boundary.api.event import Event

def createEvent(apiHost,
                apiKey,
                fingerprintFields,
                title,
                organizationID,
                source = {'ref': platform.node(),'type': 'host'},
                severity=Event.INFO,
                sender={'ref': platform.node(),'type': 'host'},
                properties=None,
                status=Event.OK,
                tags=None,
                message=None,
                createdAt=None,
                receivedAt=None,
                eventId=None):
    c = EventConnection(apiKey=apiKey,organizationID=organizationID,apiHost=apiHost)
    
    e = Event(source,
              fingerprintFields,
              title,
              organizationID,
              severity,
              sender,
              properties,
              status,
              tags,
              message,
              createdAt,
              receivedAt,
              eventId)
    
    print(c.createEvent(e))
    
    
def getEvent():
    pass
    

__all__ = ['createEvent','getEvent']

if __name__ == '__main__':
    createEvent()



