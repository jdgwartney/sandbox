#!/usr/bin/env python3

from boundary.api.event import createEvent
from boundary.api.event import getEvent


myApiHost = 'api.boundary.com'
myOrganizationID = '3ehRi7uZeeaTN12dErF5XOnRXjC'
myApiKey = 'ARI0PzUzWYUo7GG1OxiHmABTpr9'
myFingerprintFields = '@title'
myTitle = 'My shiny new event'


#
# Create a new boundary Event
#
eventId = createEvent(myApiHost,
                      myApiKey,
                      myFingerprintFields,
                      myTitle,myOrganizationID)
print('event id: ' + eventId)

#
# Fetch the newly created boundary event
#
newEvent = getEvent(myApiHost,
                    myApiKey,
                    eventId)
print(newEvent)

