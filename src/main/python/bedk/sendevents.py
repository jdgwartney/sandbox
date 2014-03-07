#!/usr/bin/env python3

from boundary.api.event import createEvent



myOrganizationID = '3ehRi7uZeeaTN12dErF5XOnRXjC'
myApiKey = 'ARI0PzUzWYUo7GG1OxiHmABTpr9'
myFingerprintField = '@title'
myTitle = 'My shiny new event'
mySource = 'boundary API'


createEvent(myOrganizationID,myApiKey,myFingerprintField,mySource,myTitle)
