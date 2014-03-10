'''
Created on Mar 4, 2014

@author: davidg
'''
from enum import Enum
import json
import platform

#
# TODO: Rethink the use of the enumerated types in the Event class for identifying fields
#
"""
Define class the enumerates each of the values for severity
"""
class SEVERITY(Enum):
        INFO = 'INFO'
        WARN = 'WARN'
        ERROR = 'ERROR'
        CRITICAL = 'CRITICAL'

"""
"""
class STATUS(Enum):
        OPEN = 'OPEN'
        CLOSED = 'CLOSED'
        ACKNOWLEDGED = 'ACKNOWLEDGED'
        OK = 'OK'

"""
Enumeration Class that defines all
of the fields of a RAW_EVENT
"""
class RAW_EVENT(Enum):
    ID = 'id'
    ORGANIZATION_ID = 'organizationID'
    SEVERITY = 'severity'
    SOURCE = 'source'
    SENDER = 'sender'
    PROPERTIES = 'properties'
    STATUS = 'status'
    FINGERPRINT_FIELDS = 'fingerprintFields'
    TAGS = 'tags'
    TITLE = 'title'
    MESSAGE = 'message'
    CREATED_AT = 'createdAt'
    RECEIVED_AT = 'receivedAt'
    EVENT_ID = 'eventId'


"""
Enumeration Class that defines all
of the fields of an EVENT
"""
class EVENT(Enum):
    ID = 'id'
    ORGANIZATION_ID = 'organizationID'
    SEVERITY = 'severity'
    SOURCE = 'source'
    SENDER = 'sender'
    PROPERTIES = 'properties'
    STATUS = 'status'
    FINGERPRINT_FIELDS = 'fingerprintFields'
    TAGS = 'tags'
    TITLE = 'title'
    MESSAGE = 'message'
    TIMES_SEEN = 'timesSeen'
    FIRST_SEEN_AT = 'firstSeenAt'
    LAST_SEEN_AT = 'lastSeenAt'
    LAST_UPDATE_AT = 'lastUpdatedAt'
    RELATED_SOURCES = 'relatedSources'
 

    __ORGANIZATION_ID_LENGTH = 27


class Event(object):
    '''
    Defines the core Boundary Event
    '''
    
    #
    # Define severity values that can be reference
    # through an Event object
    #
    CRITICAL = SEVERITY.CRITICAL.value
    INFO = SEVERITY.INFO.value
    ERROR = SEVERITY.ERROR.value
    WARN = SEVERITY.WARN.value
    
    #
    # Define status values that can be reference
    # through an Event object
    #
    OPEN = STATUS.OPEN.value
    CLOSED = STATUS.CLOSED.value
    ACKNOWLEDGED = STATUS.ACKNOWLEDGED.value
    OK = STATUS.OK.value
    
    #
    # Define our default values for fields
    # so they only have to be changed in a single
    # place. Make them private members by the "__"
    #
    __DEFAULT_ORGANIZATION_ID = None
    __DEFAULT_SEVERITY = SEVERITY.INFO.value
    __DEFAULT_SOURCE = { "ref": platform.node(),"type": "host"}
    __DEFAULT_SENDER = { "ref": platform.node(),"type": "host"}
    __DEFAULT_PROPERTIES = None
    __DEFAULT_STATUS = STATUS.OK.value
    __DEFAULT_FINGERPRINT_FIELDS = ['@title']
    __DEFAULT_TAGS = None
    __DEFAULT_TITLE = 'Boundary Event API Event'
    __DEFAULT_MESSAGE = None
    __DEFAULT_CREATED_AT = None
    __DEFAULT_RECEIVED_AT = None
    __DEFAULT_EVENT_ID = None

    def __init__(self,
                 source,
                 fingerprintFields,
                 title,
                 organizationID=__DEFAULT_ORGANIZATION_ID,
                 severity=__DEFAULT_SEVERITY,
                 sender = __DEFAULT_SENDER,
                 properties = __DEFAULT_PROPERTIES,
                 status = __DEFAULT_STATUS,
                 tags = __DEFAULT_TAGS,
                 message = __DEFAULT_MESSAGE,
                 createdAt = __DEFAULT_CREATED_AT,
                 receivedAt = __DEFAULT_RECEIVED_AT,
                 eventId =__DEFAULT_EVENT_ID):
        """
        Constructor
        
        Required Parameters:
            source
            fingerprintFields
            title
            
        Optional Parameters:
            TODO: Complete documentation
        """
        
        #
        # Create a dictionary of the values
        #
        self.__event ={}
        self.organizationID = organizationID
        self.severity = severity
        self.source = source
        self.sender = sender
        self.properties = properties
        self.status = status
        self.fingerprintFields = fingerprintFields
        self.tags = tags
        self.title = title
        self.message = message
        self.createdAt = createdAt
        self.receivedAt = receivedAt
   
    @staticmethod
    def validateOrganizationalID(organizationID):
        """
        validateOrganizationID -> Bool
        Checks to see if the organizational ID is of the correct format
        Returns:
            True - organizational id is valid
            False - organization id is invalid
            
        NOTE: Defining this method as static because might be useful in other areas
        """
        # TODO: This should be elsewheres
        __ORGANIZATION_ID_LENGTH = 27

        return len(organizationID) == __ORGANIZATION_ID_LENGTH
    
    @property
    def organizationID(self):
        return self.__event[RAW_EVENT.ORGANIZATION_ID.value]
    
    @organizationID.setter
    def organizationID(self,organizationID):
        """
        Set the organization ID of the event
        Can we set this by alias which maps to a specific organization ID and organization name
        TODO: What happens if the API key does not give access to that organization
        
        The associated organization id for this event. If not specified, organization id will be populated from the URI.
        """
        self.__event[RAW_EVENT.ORGANIZATION_ID.value] = organizationID
# TODO: Additional validation of organization ID
#         if (Event.validateOrganizationalID(organizationID) == True):
#             self.__organizationID=organizationID
#         else:
#             print("raise ValueError")
#             raise ValueError
        
    @organizationID.deleter
    def organizationID(self):
        """
        TODO: Roll out to the other attributes??
        """
        raise AttributeError("Cannot delete the organizationID attribute")
    
    @property
    def severity(self):
        """
        severity accessor
        """
        return self.__event[RAW_EVENT.SEVERITY.value]
    
    @severity.setter
    def severity(self,severity):
        """
        One of INFO, WARN, ERROR, CRITICAL. Default is INFO.
        """
        self.__event[RAW_EVENT.SEVERITY.value] = severity
        
    @property
    def source(self):
        return self.__event[RAW_EVENT.SOURCE.value]

    def __convertToSource(self,value):
        """
        
        Help function that takes various data types and converts to Event Source type
        """
        # TODO: How to handle if the call just passes in a single string
        #       The string value passed in can be REF but what is the type??
        # TODO: How to handle int, float, complex??
        if isinstance(value,str):
            theSource = {'ref':value,'type': 'host'}
        else:
            theSource = value
        return theSource

    
    @source.setter
    def source(self,source):
        """
        """
        self.__event[RAW_EVENT.SOURCE.value] = self.__convertToSource(source)
    
    @property
    def sender(self):
        """
        One of OPEN, CLOSED, ACKNOWLEDGED, or OK. Default is OK. Events with status
        OPEN, CLOSED, or ACKNOWLEDGED are able to be modified by the user,
        while OK status events are purely informational.
        """
        return self.__event[RAW_EVENT.SENDER.value]
    
    @sender.setter
    def sender(self,sender):
        self.__event[RAW_EVENT.SENDER.value] = self.__convertToSource(sender)
        
    @property
    def properties(self):
        return self.__event[RAW_EVENT.PROPERTIES.value]
    
    @properties.setter
    def properties(self,properties):
        self.__event[RAW_EVENT.PROPERTIES.value] = properties
        
    @property
    def status(self):
        return self.__event[RAW_EVENT.STATUS.value]
    
    @status.setter
    def status(self,status):
        """
        One of OPEN, CLOSED, ACKNOWLEDGED, or OK. Default is OK.
        Events with status OPEN, CLOSED,or ACKNOWLEDGED are able
        to be modified by the user, while OK status events are purely informational.
        """
        self.__event[RAW_EVENT.STATUS.value] = status
    
    @property
    def fingerprintFields(self):
        return self.__event[RAW_EVENT.FINGERPRINT_FIELDS.value]
    
    @fingerprintFields.setter
    def fingerprintFields(self,fingerprintFields):
        """
        The fields of the event used to calculate the event fingerprint.
        In this field, @title refers to RawEvent.title,
        @message refers to RawEvent.message, and all other field values come
        from the properties object. Each field must have a non-null,
        non-empty field value with a basic type (string, number, or bool).
        """
        if isinstance(fingerprintFields,str):
            fp = [fingerprintFields]
        else:
            fp = fingerprintFields
        self.__event[RAW_EVENT.FINGERPRINT_FIELDS.value] = fp
        
    @property
    def tags(self):
        """
        tags accessor
        """
#         return self.__tags
        return self.__event[RAW_EVENT.TAGS.value]
        
    @tags.setter
    def tags(self, tags):
        self.__event[RAW_EVENT.TAGS.value] = tags
        
        
    @property
    def title(self):
        """
        Description of the event. Maximum 255 characters.
        """
        return self.__event[RAW_EVENT.TITLE.value]
    
    @title.setter
    def title(self,title):
        self.__event[RAW_EVENT.TITLE.value] = title
    
    @property
    def message(self):
        """
        Additional description of the event. Maximum 255 characters.
        """
        return self.__event[RAW_EVENT.MESSAGE.value]
    
    @message.setter
    def message(self,message):
        self.__event[RAW_EVENT.MESSAGE.value] = message
        
    @property
    def createdAt(self):
        """
        The timestamp the event was created. If not specified, this is set to the time the event is received.
        """
        return self.__event[RAW_EVENT.CREATED_AT.value]
    
    @createdAt.setter
    def createdAt(self,createdAt):
        self.__event[RAW_EVENT.CREATED_AT.value] = createdAt
        
    @property
    def receivedAt(self):
        """
        The timestamp the event was received.
        """
        return self.__event[RAW_EVENT.RECEIVED_AT.value]
    
    @receivedAt.setter
    def receivedAt(self,receivedAt):
        self.__event[RAW_EVENT.RECEIVED_AT.value] = receivedAt
        
    @property
    def eventId(self):
        """
        The id of the Event this raw event was de-duplicated to.
        """
        return self.__event[RAW_EVENT.EVENT_ID.value]
    
    @eventId.setter
    def eventId(self,eventId):
        self.__event[RAW_EVENT.EVENT_ID.value] = eventId
    
    @staticmethod
    def getDefaultEvent():
        return Event(Event.__DEFAULT_SOURCE,
                     Event.__DEFAULT_FINGERPRINT_FIELDS,
                     Event.__DEFAULT_TITLE)
        
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return str(self.__event)
        
    def getActiveFields(self):
        """
        Extract the active fields from our list of fields 
        """
        e = {}
        #
        # Explictly add the required fields
        #
        e[RAW_EVENT.SOURCE.value] = self.__event[RAW_EVENT.SOURCE.value]
        e[RAW_EVENT.FINGERPRINT_FIELDS.value] = self.__event[RAW_EVENT.FINGERPRINT_FIELDS.value]
        e[RAW_EVENT.TITLE.value] = self.__event[RAW_EVENT.TITLE.value]
        
#         for f in self.__event.keys():
#             if self.__event[f] != None:
#                 e[f] = self.__event[f]
                
#         print(json.dumps(e))
        return e



        

    
        
        
    