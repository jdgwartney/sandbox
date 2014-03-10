'''
Created on Mar 6, 2014

@author: davidg
'''

from boundary.api.event import Event
from boundary.api.event import EventConnection
        
def main():
    k = 'ARI0PzUzWYUo7GG1OxiHmABTpr9'
    o = '3ehRi7uZeeaTN12dErF5XOnRXjC'
    connection = EventConnection(apiKey=k,organizationID=o)
    event = Event.getDefaultEvent()
    
    event.message = 'Hello World'
    event.title = 'Boundary Object Oriented Event API'
    
    eventId = connection.createEvent(event)
    
    print('event id: ' + str(eventId))
    
    newEvent = connection.getEvent(eventId)
    
    print('event: ' + newEvent)

if __name__ == '__main__':
    main()
