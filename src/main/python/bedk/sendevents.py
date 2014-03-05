#!/usr/bin/env python3

import boundary.api.Event as events



myOrganizationID = '3ehRi7uZeeaTN12dErF5XOnRXjC'
myApiKey = 'ARI0PzUzWYUo7GG1OxiHmABTpr9'
myFingerprintField = '@title'
myTitle = 'My shiny new event'
mySource = 'boundary API'


events.createEvent(myOrganizationID,myApiKey,myFingerprintField,mySource,myTitle)
