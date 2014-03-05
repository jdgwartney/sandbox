#!/usr/bin/env python3

import boundary.api.events



myOrganizationID = "<Organization ID>"
myApiKey = "<API key>"


boundary.api.events.createEvent(organizationID=myOrganizationID,apiKey=myApiKey)
