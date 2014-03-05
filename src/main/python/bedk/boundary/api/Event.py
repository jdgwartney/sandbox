'''
Created on Mar 4, 2014

@author: davidg
'''
from enum import Enum
"""
Define class the enumerates each of the values for severity
"""
class SEVERITY(Enum):
        INFO = 'INFO'
        WARN = 'WARN'
        ERROR = 'ERROR'
        CRITICAL = 'CRITICAL'
        
class STATUS(Enum):
        OPEN = 'OPEN'
        CLOSED = 'CLOSED'
        ACKNOWLEDGED = 'ACKNOWLEDGED'
        OK = 'OK'

class Event(object):
    '''
    Defines the core Boundary Event
    '''
    
    #
    # Define severity values that can be reference
    # through an Event object
    #
    CRITICAL = SEVERITY.CRITICAL
    INFO = SEVERITY.INFO
    ERROR = SEVERITY.ERROR
    WARN = SEVERITY.WARN
    
    #
    # Define status values that can be reference
    # through an Event object
    #
    OPEN = STATUS.OPEN
    CLOSED = STATUS.CLOSED
    ACKNOWLEDGED = STATUS.ACKNOWLEDGED
    OK = STATUS.OK
    
    #
    # Define our default values for fields
    # so they only have to be changed in a single
    # place. Make them private members by the "__"
    #
    __DEFAULT_ORGANIZATION_ID = None
    __DEFAULT_SEVERITY = SEVERITY.INFO
#    __DEFAULT_SOURCE = ''
    __DEFAULT_SENDER = None
    __DEFAULT_PROPERTIES = None
    __DEFAULT_STATUS = STATUS.OK
#    __DEFAULT_FINGERPRINT_FIELDS = ''
    __DEFAULT_TAGS = None
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
        """
        self.__organizationID = organizationID
        self.__severity = severity
        self.__source = source
        self.__sender = sender
        self.__properties = properties
        self.__status = status
        self.__fingerprintFields = fingerprintFields
        self.__tags = tags
        self.__title = title
        self.__message = message
        self.__createdAt = createdAt
        self.__receivedAt = receivedAt
        
    @property
    def organizationID(self):
        return self.__organizationID
    
    @organizationID.setter
    def organizationID(self,organizationID):
        """
        Set the organization ID of the event
        Can we set this by alias which maps to a specific organization ID and organization name
        TODO: What happens if the API key does not give access to that organization
        
        The associated organization id for this event. If not specified, organization id will be populated from the URI.
        """
        self.__organizationID=organizationID
    
    @property
    def severity(self):
        """
        severity accessor
        """
        return self.__severity
    
    @severity.setter
    def severity(self,severity):
        """
        One of INFO, WARN, ERROR, CRITICAL. Default is INFO.
        """
        self.__severity = severity
        
    @property
    def source(self):
        return self.__source
    
    @source.setter
    def source(self,source):
        self.__source = source
    
    @property
    def sender(self):
        """
        One of OPEN, CLOSED, ACKNOWLEDGED, or OK. Default is OK. Events with status
        OPEN, CLOSED, or ACKNOWLEDGED are able to be modified by the user,
        while OK status events are purely informational.
        """
        return self.__sender
    
    @sender.setter
    def sender(self,sender):
        self.__sender = sender
        
    @property
    def properties(self):
        return self.__properties
    
    @properties.setter
    def properties(self,properties):
        self.__properties = properties
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self,status):
        """
        One of OPEN, CLOSED, ACKNOWLEDGED, or OK. Default is OK.
        Events with status OPEN, CLOSED,or ACKNOWLEDGED are able
        to be modified by the user, while OK status events are purely informational.
        """
        self.__status = status
    
    @property
    def fingerprintFields(self):
        return self.__fingerprintFields
    
    @fingerprintFields.setter
    def fingerprintFields(self,fingerprintFields):
        """
        The fields of the event used to calculate the event fingerprint.
        In this field, @title refers to RawEvent.title,
        @message refers to RawEvent.message, and all other field values come
        from the properties object. Each field must have a non-null,
        non-empty field value with a basic type (string, number, or bool).
        """
        self.__fingerprintFields = fingerprintFields
        
    @property
    def tags(self):
        """
        tags accessor
        """
        return self.__tags
        
    @tags.setter
    def tags(self, tags):
        self.__tags = tags
        
    @property
    def title(self):
        """
        Description of the event. Maximum 255 characters.
        """
        return self.__title
    
    @title.setter
    def title(self,title):
        self.__title = title
    
    @property
    def message(self):
        """
        Additional description of the event. Maximum 255 characters.
        """
        return self.__message
    
    @message.setter
    def message(self,message):
        self.__message = message
        
    @property
    def createdAt(self):
        """
        The timestamp the event was created. If not specified, this is set to the time the event is received.
        """
        return self.__createdAt
    
    @createdAt.setter
    def createdAt(self,createdAt):
        self.__createdAt = createdAt
        
    @property
    def receivedAt(self):
        """
        The timestamp the event was received.
        """
        return self.__createdAt
    
    @receivedAt.setter
    def receivedAt(self,receivedAt):
        self.__receivedAt = receivedAt
        
    @property
    def eventId(self):
        """
        The id of the Event this raw event was de-duplicated to.
        """
        return self.__eventId
    
    @eventId.setter
    def eventId(self,eventId):
        self.__eventId = eventId
        

    
        
        
    