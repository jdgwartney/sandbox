#
# events.py
#
""" API for creating Boundary Events
"""
from enum import Enum
import unittest

"""
Define severity values
"""
class SEVERITY(Enum):
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

"""
Define status values
"""
class STATUS(Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    ACKNOWLEDGED = 'ACKNOWLEDGED'
    OK = 'OK' 

"""
Define fields of our RawEvents
"""
class RawEvent(Enum):
    ID = 'id'
    ORGANIZATION_ID = 'organizationID'
    SEVERITY = 'severity'
    SOURCE = 'source'
    SENDER = 'sender'
    


#
# Define default values for Boundary Events
#
__DEFAULT_SEVERITY = SEVERITY.INFO
__DEFAULT_SOURCE = 'boundary.api'
__DEFAULT_SENDER = None
__DEFAULT_PROPERTIES = None
__DEFAULT_STATUS = STATUS.OK
__DEFAULT_TAGS = None
__DEFAULT_TITLE = None
__DEFAULT_MESSAGE = None
__DEFAULT_CREATED_AT = None
__DEFAULT_RECEIVED_AT = None
__DEFAULT_EVENT_ID = None


#
# Define default configuration values
#
__DEFAULT_API_HOST='api.boundary.com'
__DEFAULT_EVENT_PATH='events'

#
# Define all of the parameters that are required
# first since they are required. Use default values for
# the parameters for the rest
#
def createEvent(organizationID,
                apiKey,
                fingerprintFields,
                title,
                source,
                severity=__DEFAULT_SEVERITY,
                sender=__DEFAULT_SENDER,
                properties=__DEFAULT_PROPERTIES,
                status=__DEFAULT_STATUS,
                tags=__DEFAULT_TAGS,
                message=__DEFAULT_MESSAGE,
                createdAt=__DEFAULT_CREATED_AT,
                receivedAt=__DEFAULT_RECEIVED_AT):
    """
    creatEvent(organizationID,apiKey,...) -> String
    
    Required arguments:
        organizationID - The associated organization id for this event.
                         If not specified, organization id will be populated from the URI.
        apiKey - One of INFO, WARN, ERROR, CRITICAL. Default is INFO.
        fingerprintFields - The fields of the event used to calculate the event fingerprint.
                            In this field, @title refers to RawEvent.title, @message refers to RawEvent.message,
                            and all other field values come from the properties object.
                            Each field must have a non-null, non-empty field value
                            with a basic type (string, number, or bool).
        source - The source of the event. The source is typically the hostname
                 or ip address of the system this event refers to.
        title - Description of the event. Maximum 255 characters.
    Optional arguments:
        severity - One of INFO, WARN, ERROR, CRITICAL. Default is INFO.
        sender - Optional information about the sender of the event.
                 This is used to describe a third party event system
                 forwarding this event into Boundary,
                 or a Boundary service sending the event.
        properties - Properties for the event.
        status - One of OPEN, CLOSED, ACKNOWLEDGED, or OK. Default is OK.
                 Events with status OPEN, CLOSED, or ACKNOWLEDGED
                 are able to be modified by the user,
                 while OK status events are purely informational.
        tags - Tags used to provide a classification for events.
               There is a configurable maximum number of allowed tags
               per event (default is 100).
        message - Additional description of the event. Maximum 255 characters.
        createdAt - The timestamp the event was created.
                    If not specified, this is set to the time the event is received.
        receivedAt - The timestamp the event was received.
    
    """
    #
    # Print out the event default arguments
    #
    print("'{0}' '{1}' '{2}' '{3}'".format(organizationID,apiKey,fingerprintFields,title))
    
    # Create a dictionary of
    event = __event(organizationID,
                        apiKey,
                        fingerprintFields,
                        title,
                        source,
                        severity,
                        sender,
                        properties,
                        status,
                        tags,
                        message,
                        createdAt,
                        receivedAt)
    
    json = __eventToJSON(event)
    uri = __buildURI(__DEFAULT_API_HOST,organizationID,__DEFAULT_EVENT_PATH)
    eventID = __sendEvent(uri,json)

def __event(organizationID,
                apiKey,
                fingerprintFields,
                title,
                source,
                severity,
                sender,
                properties,
                status,
                tags,
                message,
                createdAt,
                receivedAt):
    """
    Create an event 'dictionary'
    """
    event = {RawEvent.ORGANIZATION_ID : organizationID,
             RawEvent.SEVERITY: severity,
             RawEvent.SOURCE: source}
    return event
 
    
    
    
def __buildURI(apiHost,organizationID,eventPath):
    """
    Generate the URI required for the REST call
    """
    #
    # Format the URI
    #
    uri = 'https://{0}/{1}/{2}'.format(apiHost,organizationID,eventPath)
    return uri

def __setAuthHeader(apiKey):
    """
    """
    print(apiKey)

def __eventToJSON(event):
    """
    Transform event fields dictionary into a JSON payload
    """
    print(event)
    
def __sendEvent(uri,jsonEvent):
    """
    Sends an event to the boundary server using the boundary RESET API
    """
    print('uri: {0}{1}json: {2}'.format(uri,'\n',jsonEvent))
    return '9999'

"""
Tests to validate the functional boundary API
"""
class TestEventAPI(unittest.TestCase):
    
    def setUp(self):
        """
        Setup the needed scaffolding for testing:
        Dummy Event
        """
        # Create an event for scaffolding
        self.__event = {RawEvent.ORGANIZATION_ID : RawEvent.ORGANIZATION_ID,
        RawEvent.SEVERITY: RawEvent.SEVERITY,
        RawEvent.SOURCE: RawEvent.SOURCE}
        
        # Create a json string to validate against
        self.__json = 'foo'

        pass

    def tearDown(self):
        pass
    
    def testURI(self):
        pass
    
    def testEventToJSON(self):
        pass
#         json = __eventToJSON(self.__event)
#         self.assertEqual(self.__json,json)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

